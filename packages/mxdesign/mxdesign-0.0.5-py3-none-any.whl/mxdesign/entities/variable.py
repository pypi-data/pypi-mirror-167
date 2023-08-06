"""Variable"""
import enum
import re

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, UniqueConstraint, CheckConstraint, column, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, object_session

from mxdesign.entities.base import Base
from mxdesign.entities.value import ValueType, Value

name_pattern = re.compile(r'[_A-Za-z][_A-Za-z0-9]*')


class VariableType(enum.Enum):
    """VariableType"""
    independent = 1
    dependent = 2
    controlled = 3
    extraneous = 3


class Variable(Base):
    """Namespace"""
    __tablename__ = 'variable'

    id = Column(Integer, primary_key=True)
    namespace_id = Column(Integer, ForeignKey('namespace.id'), nullable=False)
    name = Column(String(64), nullable=False)
    multistep = Column(Boolean, nullable=True)
    vtype = Column('vtype', Enum(VariableType), nullable=True)
    _dtype = Column('dtype', Enum(ValueType), nullable=True)

    namespace = relationship('Namespace', back_populates='variables')
    values = relationship('Value', back_populates='variable')

    __table_args__ = (
        UniqueConstraint('namespace_id', 'name'),
        CheckConstraint(column('name').regexp_match('^[_A-Za-z][_A-Za-z0-9]*$')),
    )

    def __init__(self, dtype=None, **kwargs):
        super(Variable, self).__init__(**kwargs)
        self.dtype = dtype

    @hybrid_property
    def dtype(self):
        """Data type of the variable.

        Returns
        -------
        dtype: type or None
        """
        if self._dtype is None:
            return None
        if self._dtype == ValueType.int:
            return int
        elif self._dtype == ValueType.float:
            return float
        elif self._dtype == ValueType.string:
            return str
        raise KeyError('invalid dtype')

    @dtype.setter
    def dtype(self, value):
        if value is None:
            self._dtype = None
        elif isinstance(value, ValueType):
            self._dtype = value
        elif isinstance(value, type):
            self._dtype = ValueType[value.__name__]
        elif isinstance(value, str):
            self._dtype = ValueType[value]
        else:
            self._dtype = ValueType(value)

    def __call__(self, value=None, **kwargs):
        """Create a value from variable."""
        session = object_session(self)
        if value is not None:
            if not isinstance(value, (str, int, float)):
                raise TypeError('expected a string, int or float, found {}'.format(type(value)))
            if self.dtype is not None and not isinstance(value, self.dtype):
                raise TypeError('expected value type {} for variable {}, found {}'.format(
                    self.dtype.__name__,
                    self.name,
                    type(value).__name__,
                ))
            # setup the dtype param of variable based on data
            if self.dtype is None:
                self.dtype = type(value)
        # setup the multistep param of variable based on data
        step = kwargs.get('step')
        if self.multistep is None:
            self.multistep = step is not None
        elif self.multistep != (step is not None):
            # multistep is true + current step value is none
            if self.multistep:
                raise TypeError('__call__() missing keyword argument \'step\' in a multistep variable')
            else:
                raise TypeError('__call__() unexpected keyword argument \'step\' in a non-multistep variable')
        # check if the created will be unique
        if kwargs.get('trial_id') is not None:
            trial_id = kwargs['trial_id']
            query = session.query(Value) \
                .filter(Value.variable_id == self.id) \
                .filter(Value.trial_id == trial_id)
            if step is not None:
                query = query \
                    .filter(Value.step == step)
            if query.first() is not None:
                raise TypeError('found value for variable {} in trial {}'.format(
                    self.name,
                    trial_id,
                ))
        # create value of variable in trial context (if provided)
        result = Value(value=value, variable=self, **kwargs)
        session.add(result)
        session.commit()
        return result

    def __repr__(self):
        return 'Variable(id={}, name={}, vtype={}, dtype={})'.format(
            self.id,
            self.name,
            'None' if self.vtype is None else self.vtype.__name__,
            self.dtype.__name__,
        )

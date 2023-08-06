"""Value"""
import enum

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, validates

from mxdesign.entities.base import Base, TimestampMixin


class ValueType(enum.Enum):
    """VariableType"""
    int = 1
    float = 2
    string = 3


class Value(TimestampMixin, Base):
    """Value"""
    __tablename__ = 'value'

    id = Column(Integer, primary_key=True)
    trial_id = Column(Integer, ForeignKey('trial.id'), nullable=False)
    variable_id = Column(Integer, ForeignKey('variable.id'), nullable=False)
    step = Column(Integer, nullable=True)
    _value = Column('value', String)

    trial = relationship('Trial', back_populates='values')
    variable = relationship('Variable', back_populates='values')

    __table_args__ = (
        UniqueConstraint('trial_id', 'variable_id', 'step'),
    )

    def __init__(self, value, **kwargs):
        super(Value, self).__init__(**kwargs)
        self.value = value

    @validates('trial_id', 'variable_id', 'step')
    def _validate_step(self, key, value):
        if key == 'step':
            step_is_not_none = value is not None
            if self.variable.multistep != step_is_not_none:
                if self.variable.multistep:
                    raise TypeError('missing \'step\' in a multistep variable')
                else:
                    raise TypeError('unexpected \'step\' in a non-multistep variable')
        return value

    @hybrid_property
    def value(self):
        """Take the value.

        Returns
        -------
        value: int or float or str

        """
        # return as the type of the variable
        return self.variable.dtype(self._value)

    @value.setter
    def value(self, value):
        # try to typecast to the accepted variable type
        var_value = self.variable.dtype(value)
        self._value = str(var_value)

    def __repr__(self):
        return 'Value(id=({}, {}), name={}, value={}, step={}, dtype={})'.format(
            self.trial_id,
            self.variable_id,
            self.variable.name,
            self.value,
            self.step,
            self.variable.dtype.__name__,
        )

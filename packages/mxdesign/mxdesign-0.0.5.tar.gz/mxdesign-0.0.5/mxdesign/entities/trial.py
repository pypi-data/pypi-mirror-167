"""Trial"""
import pandas as pd
from sqlalchemy import Column, Integer, ForeignKey, literal
from sqlalchemy.orm import relationship, object_session, aliased

from mxdesign import utils
from mxdesign.entities.namespace import Namespace
from mxdesign.entities.variable import Variable
from mxdesign.entities.value import Value
from mxdesign.entities.base import Base


class Trial(Base):
    """Trial"""
    __tablename__ = 'trial'

    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey('experiment.id'), nullable=False)

    experiment = relationship('Experiment', back_populates='trials')  # type: 'Experiment'
    values = relationship('Value', back_populates='trial', cascade='all, delete-orphan')  # type: 'Value'

    def set(self, key, value=None, namespace=None, **kwargs):
        """Sets a variable.

        A namespace can only have one variable with same name.

        Parameters
        ----------
        key: str
            The key of the variable to set.
        value: typing.Any
            The value.
        namespace: 'Namespace'
            The namespace to place the variable.
        Returns
        -------
        value: Value
            Set value.
        """
        if value is None and isinstance(key, pd.DataFrame):
            value = key
            key = None
        if isinstance(value, pd.DataFrame):
            values = []
            for data in utils.from_frame(value):
                namepath = ()
                if namespace is not None:
                    namepath += namespace,
                if key is not None:
                    namepath += key,
                if data.get('namespace') is not None:
                    namepath += data.get('namespace'),
                data['namespace'] = '.'.join(namepath)
                values += self.set(**data, **kwargs),
            return values
        else:
            session = object_session(self)
            namespace = self.experiment.namespace[namespace]
            # create or update the variable
            var = session.query(Variable) \
                .filter(Variable.namespace_id == namespace.id) \
                .filter(Variable.name == key) \
                .first()
            if var is None:
                var = Variable(namespace_id=namespace.id, name=key)
                session.add(var)
                session.commit()
            return var(value, trial_id=self.id, **kwargs)

    def get(self, key, namespace=None, **kwargs):
        """Gets a variable.

        Parameters
        ----------
        key: str or 'Variable'
            The key of the variable to get. None or '*' gets all variables.
        namespace: str or 'Namespace'
            The namespace to search the variable name (key).
        Returns
        -------
        value: 'Value' or list of 'Value'
            Value/values in the namespace with the key.
        """
        session = object_session(self)
        if isinstance(key, Variable):
            var = key
            if var.multistep is None:
                raise ValueError('can\'t determine if the variable is multistep')
            query = session.query(Value) \
                .filter(Value.trial_id == self.id) \
                .filter(Value.variable_id == var.id)
            if var.multistep:
                values = query \
                    .filter(Value.step.isnot(None)) \
                    .all()
            else:
                # Note: value can be None
                values = query \
                    .filter(Value.step.is_(None)) \
                    .first()
        else:
            namespace = self.experiment.namespace[namespace]
            if key is None or key == '*':
                stack = [namespace]
                values = []
                while len(stack) > 0:
                    namespace = stack.pop()  # type: Namespace
                    query = session.query(Variable) \
                        .filter(Variable.namespace_id == namespace.id)
                    for var in query.all():
                        value = self.get(var, **kwargs)
                        if isinstance(value, list):
                            values += value
                        elif value is not None:
                            values.append(value)
                    stack += namespace.children
            else:
                var = session.query(Variable) \
                    .filter(Variable.namespace_id == namespace.id) \
                    .filter(Variable.name == key) \
                    .first()
                values = self.get(var, **kwargs)
        return values

    def __repr__(self):
        return 'Trial(id={})'.format(
            self.id,
        )

#aqui estan los formularios WTF

from flask_wtf import FlaskForm
from wtforms import DateField #importamos campos de tipo fecha, que es una clase. Y se importa de wtforms (no la de flask_wtf)
from wtforms.fields.core import BooleanField, FloatField, SelectField, StringField
from wtforms.fields.simple import HiddenField, SubmitField 
from wtforms.validators import DataRequired, Length, ValidationError 
from datetime import date

def fecha_hasta_hoy(formulario, campo):
    hoy = date.today()
    if campo.data > hoy:
        raise ValidationError('La fecha {} no puede ser mayor que {}'.format(campo.data, hoy))


class MovimientosForm(FlaskForm):
    id = HiddenField()
    fecha =  DateField('Fecha', validators=[DataRequired(message= 'formato: aaaa-mm-dd'), fecha_hasta_hoy]) #ponemos la etiqueta que queremos que tenga el campo y validadores es una lista y va en corchete
    concepto = StringField('Concepto', validators=[DataRequired(), Length(min=10)])
    categoria = SelectField('Categoria', choices=[('00', ''), ('SU', 'Supervivencia'),('OV', 'OCIO/VICIO'),('CU', 'Cultura'), ('EX', 'Extras')])
    cantidad = FloatField("Cantidad", validators=[DataRequired()])
    esGasto = BooleanField("Es gasto")
    submit = SubmitField('Aceptar')

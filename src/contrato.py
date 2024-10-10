import pandera as pa
from pandera.typing import Series


class MetricasFinanceirasBase(pa.DataFrameModel):
    setor_da_empresa: Series[str]
    receita_operacional: Series[float] = pa.Field(ge=0) #ge = Greater than or equal
    data: Series[pa.DateTime]
    percentual_de_imposto: Series[float] = pa.Field(in_range= {"min_value": 0, "max_value": 1})#Range do percentual do imposto sendo entre 0 e 1
    custos_operacionais: Series[float] = pa.Field(ge=0)#ge = Greater or equal

    class Config:
        strict = True
        coerce = True 
         #strict -> O dataframe tem que ter exatamente as colunas especificadas. A não ser que a coluna seja opcional
         #coerce -> Toda vez que a classe MetricasFinanceirasBase for utilizada, uma verificação do tipo de dado será feita, se o tipo de dado nao for o especificado, será feito uma tentativa de converter ao tipo de dado especificado.

    @pa.check(  # Validacao dos Setores no dataframe
        "setor_da_empresa",
        name = "Checagem código de setores",
        error = "Código de setor inválido")
    def checa_codigo_setor(cls, codigo:Series[str]) -> Series[bool]:
        return codigo.str[:4].isin(['REP_','MNT_','VND_']) #Verificacao dos prefixos de codigo de setores
    
class MetricasFinanceirasOut(MetricasFinanceirasBase):
    valor_do_imposto: Series[float] = pa.Field(ge=0)
    custo_total: Series[float] = pa.Field(ge=0)
    receita_liquida: Series[float] = pa.Field(ge=0)
    margem_operacional: Series[float] = pa.Field(ge=0)
    transformado_em: Optional[pa.DateTime]

    @pa.dataframe_check
    def checa_margem_operacional(cls, df:pd.DataFrame) -> Series[bool]:
        return df["margem_operacional"] == (df["receita_liquida"] / df["receita_operacional"]) #Verificacao da margem operacional
# Projeto de ETL e Validação de Qualidade de DadosProjeto de ETL e Validação de Qualidade de Dados

Este projeto implementa um pipeline de ETL (Extração, Transformação e Carga) de dados financeiros usando Pandas e Pandera para garantir a qualidade dos dados por meio de contratos de validação de schema.

### Visão Geral

Este pipeline foi desenvolvido para realizar a extração de dados financeiros a partir de arquivos CSV, transformá-los e carregá-los em um banco de dados PostgreSQL. O projeto utiliza o conceito de contrato de dados, onde o schema esperado do DataFrame é definido e validado automaticamente, assegurando que os dados processados estejam no formato correto e obedeçam às regras de negócio preestabelecidas.

### Objetivos 
Garantir a Qualidade dos Dados: Através de contratos de dados, o projeto valida o schema dos dados, assegurando que os dados carregados estão de acordo com as expectativas do modelo financeiro. Automação de ETL: O pipeline automatiza as etapas de extração, transformação e carga de dados, reduzindo erros manuais e aumentando a eficiência. Testes Automatizados: O projeto inclui testes automatizados com o Pytest para validar cenários diversos em relação ao contrato de dados.

### Referente ao Dataframe:

VND = Venda REP = Serviço de Reparacao MNT = Manutencao

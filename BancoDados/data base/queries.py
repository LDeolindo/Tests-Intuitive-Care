Montar uma query analítica que traga a resposta para as seguintes perguntas:
  - Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
  - Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?

searchByGoal = (status) => {
    const goalsFiltered = this.state.goals.filter((item) => moment(item.year).format('YYYY') === this.state.yearSearch.format('YYYY') && item.goals.map(e => e.status).includes(status));

    this.setState({ goalsFiltered, status });
  }

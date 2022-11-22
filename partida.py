
st.markdown("# 🏆 FIFA World Cup - Qatar 2022 ") 
st.markdown('---')

st.markdown("## ⚽Odds of the Matches")
st.markdown('---')

listaselecoes1 = selecoes.index.tolist()  
listaselecoes1.sort()
listaselecoes2 = listaselecoes1.copy()

j1, j2 = st.columns(2)
selecao1 = j1.selectbox('Choose the first country:', listaselecoes1) 
listaselecoes2.remove(selecao1)
selecao2 = j2.selectbox('Choose the second country.', listaselecoes2, index = 1)
st.markdown('---')

jogo = ProbabilidadesPartida(selecao1, selecao2)
prob = jogo['probabilidades']
matriz = jogo['matriz']

col1, col2, col3, col4, col5 = st.columns(5)
col1.image(selecoes.loc[selecao1, 'LinkBandeiraGrande'])  
col2.metric(selecao1, prob[0])
col3.metric('Empate / Draw', prob[1])
col4.metric(selecao2, prob[2]) 
col5.image(selecoes.loc[selecao2, 'LinkBandeiraGrande'])

st.markdown('---')
st.markdown("## 📊 Scores Odds") 

def aux(x):
	return f'{str(round(100*x,1))}%'
st.table(matriz.applymap(aux))


st.markdown('---')
st.markdown("## 🌍 World Cup Match Odds") 

jogoscopa = pd.read_excel('dados/outputEstimativasJogosCopa.xlsx', index_col = 0)
st.table(jogoscopa[['grupo', 'seleção1', 'seleção2', 'Vitória', 'Empate', 'Derrota']])


st.markdown('---')

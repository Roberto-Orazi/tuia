import { Expenses } from './components/Expenses/Expenses';

const App = () => {
  const expenses = [ //aca tengo un array con objetos adentro
    {
      id: 'e1',
      title: 'Toilet Paper',
      amount: 94.12,
      date: new Date(2020, 7, 14),
    },
    {
      id: 'e2',
      title: 'New TV',
      amount: 799.49,
      date: new Date(2021, 2, 12)
    },
    {
      id: 'e3',
      title: 'Car Insurance',
      amount: 294.67,
      date: new Date(2021, 2, 28),
    },
    {
      id: 'e4',
      title: 'New Desk (Wooden)',
      amount: 450,
      date: new Date(2021, 5, 12),
    },
  ];
  return (
    <div className="App">
      <header className="App-header">
        <h1>Expensas</h1>
        <Expenses items={expenses} />
      </header>
    </div>
  );
}
/*
return(
React.createElement('div',{})
React.createElement('h2',{},'Expensas')
React.createElement(Expenses,{items: expenses})
)
*/
export default App;

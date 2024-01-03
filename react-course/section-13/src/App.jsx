import { useState } from 'react';

import Counter from './components/Counter/Counter.jsx';
import Header from './components/Header.jsx';
import { log } from './log.js';
import ConfigueCounter from './components/Counter/ConfigureCounter.jsx';

function App() {
  log('<App /> rendered');

  const [chosenCount, setChosenCount] = useState(0);

  function handleSetCount(newCount) {
    setChosenCount(newCount)
  }

  return (
    <>
      <Header />
      <main>
        <ConfigueCounter onset={handleSetCount} />
        <Counter initialCount={chosenCount} />
        <Counter initialCount={0} />
      </main >
    </>
  );
}

export default App;

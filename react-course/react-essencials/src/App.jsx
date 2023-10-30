import { CoreConcept } from "./components/CoreConcept";
import { Header } from "./components/Header/Header";
import { TabButton } from "./components/TabButton";
import { CORE_CONCEPTS } from "./Data/data";

function App() {
  let tabContent = 'Click a button'
  const handleSelect = (selectedButton) => {
    tabContent = selectedButton
  }
  return (
    <div>
      <Header />
      <main>
        <section id="core-concepts">
          <h2>Core Concepts</h2>
          <ul>
            <CoreConcept
              title={CORE_CONCEPTS[0].title}
              description={CORE_CONCEPTS[0].description}
              image={CORE_CONCEPTS[0].image} />
            <CoreConcept {...CORE_CONCEPTS[1]} />
            <CoreConcept {...CORE_CONCEPTS[2]} />
            <CoreConcept {...CORE_CONCEPTS[3]} />
          </ul>
        </section>
        <section id='examples'>
          <h2>Examples</h2>
          <menu>
            <TabButton onSelect={() => handleSelect('components')}>
              Components
            </TabButton>
            <TabButton onSelect={() => handleSelect('jsx')}>
              JSX
            </TabButton>
            <TabButton onSelect={() => handleSelect('props')}>
              Props
            </TabButton>
            <TabButton onSelect={() => handleSelect('state')}>
              State
            </TabButton>
          </menu>
          {tabContent}
        </section>
      </main>
    </div>
  );
}

export default App;
import React, { useState } from "react";
import { CoreConcept } from "./components/CoreConcept";
import { Header } from "./components/Header/Header";
import { TabButton } from "./components/TabButton";
import { CORE_CONCEPTS, EXAMPLES } from "./Data/data";
import { TabContent } from "./components/TabContent";

function App() {
  const [selectedTopic, setSelectedTopic] = useState('components')

  const handleSelect = (selectedButton) => {
    setSelectedTopic(selectedButton)
  }
  let tabContent = <p>Please select a topic.</p>
  if (selectedTopic) {
    tabContent = (
      <div id="tab-content">
        <TabContent
          title={EXAMPLES[selectedTopic].title}
          description={EXAMPLES[selectedTopic].description}
          code={EXAMPLES[selectedTopic].code} />
      </div>
    )
  }
  return (
    <div>
      <Header />
      <main>
        <section id="core-concepts">
          <h2>Core Concepts</h2>
          <ul>
            {CORE_CONCEPTS.map((conceptItem) => <CoreConcept key={conceptItem.title} {...conceptItem} />)}
            {/*  <CoreConcept
              title={CORE_CONCEPTS[0].title}
              description={CORE_CONCEPTS[0].description}
              image={CORE_CONCEPTS[0].image} />
            <CoreConcept {...CORE_CONCEPTS[1]} />
            <CoreConcept {...CORE_CONCEPTS[2]} />
            <CoreConcept {...CORE_CONCEPTS[3]} /> */}
          </ul>
        </section>
        <section id='examples'>
          <h2>Examples</h2>
          <menu>
            <TabButton isSelected={selectedTopic == 'components'} onSelect={() => handleSelect('components')}>
              Components
            </TabButton>
            <TabButton isSelected={selectedTopic == 'jsx'} onSelect={() => handleSelect('jsx')}>
              JSX
            </TabButton>
            <TabButton isSelected={selectedTopic == 'props'} onSelect={() => handleSelect('props')}>
              Props
            </TabButton>
            <TabButton isSelected={selectedTopic == 'state'} onSelect={() => handleSelect('state')}>
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
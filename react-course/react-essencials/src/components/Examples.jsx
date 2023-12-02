import React, { useState } from "react"
import { TabButton } from "./TabButton"
import { EXAMPLES } from "../Data/data"
import { TabContent } from "./TabContent"
import { Section } from "./Section"
import { Tabs } from "./Tabs"

export const Examples = () => {
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
        <Section id='examples' title='Examples'>
            <Tabs
                buttons={
                    <>
                        <TabButton isSelected={selectedTopic == 'components'} onClick={() => handleSelect('components')}>
                            Components
                        </TabButton>
                        <TabButton isSelected={selectedTopic == 'jsx'} onClick={() => handleSelect('jsx')}>
                            JSX
                        </TabButton>
                        <TabButton isSelected={selectedTopic == 'props'} onClick={() => handleSelect('props')}>
                            Props
                        </TabButton>
                        <TabButton isSelected={selectedTopic == 'state'} onClick={() => handleSelect('state')}>
                            State
                        </TabButton>
                    </>
                }>
                {tabContent}
            </Tabs>
        </Section>
    )
}
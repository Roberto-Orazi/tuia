import { useState } from "react";
import { NoProjectsSelected } from "./components/NoProjectsSelected";
import { SideBar } from "./components/SideBar";
import { NewProject } from "./components/NewProject";

function App() {
  const [projectsState, setProjectsState] = useState({
    selectedProjectId: undefined,
    projects: []
  })
  const handleStartAddProject = () => {
    setProjectsState(prevState => {
      return {
        ...prevState,
        selectedProjectId: null,
      }
    })
  }
  const handleAddProject = (projectData) => {
    setProjectsState(prevState => {
      const newProject = {
        ...projectData,
        id: Math.random()
      }
      return {
        ...prevState,
        projects: [...prevState.projects, newProject]
      }
    })
  }
  console.log(projectsState)
  let content
  if (projectsState.selectedProjectId === null) {
    content = <NewProject onAdd={handleAddProject}/>
  } else if (projectsState.selectedProjectId === undefined) {
    content = <NoProjectsSelected onStartAdd={handleStartAddProject} />
  }
  return (
    <main className="h-screen my-8 flex gap-8">
      <SideBar onStartAdd={handleStartAddProject} />
      {content}
    </main>
  );
}

export default App;

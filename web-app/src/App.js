import React from 'react';
import ReactMarkdown from 'react-markdown'
import SkulptRunner from './SkulptRunner';

function Code(props) {

  return <SkulptRunner code={props.value}/>
}

function App() {
  const readme = `# Hello
  This is some sort of descriptions!
  **bolded??**

  \`\`\`python3
  def hello():
    print("Hello")
  \`\`\`
  ## HEading 2
  \`\`\`\python3
  def wiegehts():
    print("wiegehts")
  wiegehts()
  \`\`\`
  `

  return (
    <div className="App">
     <ReactMarkdown renderers={{code: Code}} source={readme} />
    </div>
  );
}

export default App;

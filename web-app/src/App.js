import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown'
import SkulptRunner from './SkulptRunner';
import {LEARNING_CONTENT} from './content'
import './appstyles.css'

function Code(props) {

  return <div style={{padding: '2%', border: 'solid 1px black'}}><SkulptRunner code={props.value}/></div>
}

function App() {
  const [readmeToDisplay, setReadmeToDisplay] = useState("")

  const keys = Object.keys(LEARNING_CONTENT)

  keys.forEach(console.log)

  return (
    <div className="App">

      <ul>
        {
          keys.map(key => <li><a style={{textDecoration: 'underline', cursor: 'pointer'}} onClick={() => setReadmeToDisplay(key)}>{key}</a></li>)
        }
      </ul>

      <div style={{padding: '2%'}}>
      <ReactMarkdown renderers={{code: Code}} source={LEARNING_CONTENT[readmeToDisplay]} />
      </div>
     
    </div>
  );
}

export default App;

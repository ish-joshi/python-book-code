import React, { Component } from 'react';

import Editor from 'react-simple-code-editor';
import Prism from "prismjs";
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism-dark.css';
import 'prismjs/plugins/line-numbers/prism-line-numbers';
import 'prismjs/plugins/line-numbers/prism-line-numbers.css';

const Sk = window.Sk;

class SkulptRunner extends Component {
    constructor(props) {
        super(props);
        console.log(props)
        this.state = { 
            code: props.code || "",
            out: "",
            holding: []
         }
    }

    //@region skulpt
    builtinRead(lib) {
        console.log(lib)
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][lib] === undefined)
                throw new Error(`File not found: '${lib}'`)
        return Sk.builtinFiles["files"][lib]
    }

  

    onRun() {
        Sk.configure({output: (out) => {
            this.setState(prev => ({
                holding: prev.holding.concat([out])
            }))
        }, read: this.builtinRead, 
        __future__: Sk.python3})
Sk.misceval.asyncToPromise(() => {
            return Sk.importMainWithBody("<stdin>", false, this.state.code, true);
        }).then(() => console.log("Successs"))
        .catch((err) => console.error(err))
        
    }

    render() { 
        console.log(this.state)
        return ( <div>
        
        
        <Editor
        value={this.state.code}
        onValueChange={code => this.setState({ code })}
        highlight={code => {console.log(code); return Prism.highlight(code, Prism.languages.python, 'python')}}
        padding={10}
        style={{
          fontFamily: '"Fira code", "Fira Mono", monospace',
          fontSize: 14,
        }}
      /><br/>
      <button onClick={() => this.onRun()}>Run</button> <button onClick={() => {
          this.setState({holding: []})
      }}>Clear</button>
      <h6>Output</h6>
      <code>{this.state.holding.map(item => <CodeOutput output={item} />)}</code>
        </div> );
    }
}


function CodeOutput(props) {
    return <pre style={{margin: 0, marginBottom: 2}}>
        {props.output}
    </pre>
}
 
export default SkulptRunner;
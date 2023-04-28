import React from "react";
import "./styles.css";

function Button(props) {
  const [counter, setCounter] = React.useState(0);
  const [name, setName] = React.useState("Daffa");
  return (
    <div>
      <button onClick={() => setCounter(counter + 1)}>
        {props.btnText} {props.id}
      </button>
      <p>
        I am {name} clicked on {counter} times
      </p>
    </div>
  );
}
function App() {    
  return (
    <div>
      <p>Hello World</p>
      <Button btnText="Submit" id="20"></Button>
      <Button btnText="Save"></Button>
      <Button btnText="Cancel"></Button>
    </div>
  );
}
export default App;

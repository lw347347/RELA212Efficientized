import React from 'react';
import logo from './logo.svg';
import './App.css';
import LeftColumn from './components/LeftColumn';
import MiddleColumn from './components/MiddleColumn';
import RightColumn from './components/RightColumn';

function App() {
  return (
    <div className="App">
      <div className="mainContent">        
        <LeftColumn></LeftColumn>
        <MiddleColumn></MiddleColumn>
        <RightColumn></RightColumn>
      </div>
    </div>
  );
}

export default App;

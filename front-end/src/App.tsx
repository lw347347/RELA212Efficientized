import React from 'react';
import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import LeftColumn from './components/LeftColumn';
import MiddleColumn from './components/MiddleColumn';
import RightColumn from './components/RightColumn';
import StudyGuideImporter from './components/StudyGuideImporter';
import StudyGuides from './components/StudyGuides';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <Router>      
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/StudyGuideImporter">Import Study Guide</Link>
            </li>
            <li>
              <Link to="/StudyGuides">Study Guides</Link>
            </li>
          </ul>
        </nav>
        <div className="mainContent">        
          <LeftColumn></LeftColumn>
          <Switch>
            <Route path="/StudyGuideImporter">
              <StudyGuideImporter />
            </Route>
            <Route path="/StudyGuides">
              <StudyGuides />
            </Route>
            <Route path="/">
              <div>Home</div>
            </Route>
          </Switch>
          <RightColumn></RightColumn>
        </div>
      </div>
    </Router>

  );
}

export default App;

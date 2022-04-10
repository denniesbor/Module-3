import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import About from './components/About';
import Error from './components/Error';
import Home from './components/Home';
import Mapbox from './components/Mapbox';

function App() {
  return (
    <Router>
    <Navbar/>
      <Switch>
        <Route exact path="/">
        <Home/>
        </Route>
        <Route exact path="/about/">
        <About/>
        </Route>
        <Route exact path="/business/:id">
          < Mapbox />
        </Route>
        <Route path="*">
        <Error/>
        </Route>
      </Switch>
    </Router>
  )
}

export default App
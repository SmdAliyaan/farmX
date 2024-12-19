import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import './App.css';

const App = () => {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/login" component={Login} />
                    <Route path="/register" component={Register} />
                    <Route path="/" component={HomePage} />
                </Switch>
            </div>
        </Router>
    );
};

const HomePage = () => (
    <div>
        <h1>Welcome to FarmX</h1>
        <a href="/login">Login</a> | <a href="/register">Register</a>
    </div>
);

export default App;


import React from 'react';
import ReactDOM from 'react-dom';
import Main from './Main';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import './css/index.css';
import injectTapEventPlugin from 'react-tap-event-plugin';

injectTapEventPlugin();


const App = () => (
  <MuiThemeProvider>
    <Main />
  </MuiThemeProvider>
);

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import SearchField from './Search.js';

class MainPage extends Component {
    render() {
        return (
        <MuiThemeProvider>
            <SearchField />
        </MuiThemeProvider>);
    }
}

export default MainPage;
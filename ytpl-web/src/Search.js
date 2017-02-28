import React, {Component} from 'react';
import TextField from 'material-ui/TextField';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

class SearchField extends Component {
    render() {
        return (
            <form>
                <TextField placeholder="Search for video"/>
            </form>
        );
    }
}

class Search extends Component {
    render() {
        return (<div><MuiThemeProvider><SearchField/></MuiThemeProvider></div>)
    }
}

export default Search;
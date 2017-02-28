import React, {Component} from 'react';
import TextField from 'material-ui/TextField';

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
        return (<div><SearchField /></div>)
    }
}

export default Search;
import React, { Component } from 'react';
import TextField from 'material-ui/TextField';

class SearchField extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return (
            <form>
                <TextField placeholder="Search for video" />
            </form>
        );
    }    
}

export default SearchField;
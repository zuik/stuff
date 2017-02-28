import React, {Component} from 'react';
import AudioPlayer from './AudioPlayer';
import Search from './Search';
import './App.css';

class App extends Component {
    render() {
        return (
            <div>
                <Search />
                <AudioPlayer src="test.mp3"/>
            </div>
        );
    }
}

export default App;

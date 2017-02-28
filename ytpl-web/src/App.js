import React, {Component} from 'react';
import AudioPlayer from './AudioPlayer';
import './App.css';

class App extends Component {
    render() {
        return (
            <footer>
                <div><AudioPlayer src="test.mp3"/></div>
            </footer>
        );
    }
}

export default App;

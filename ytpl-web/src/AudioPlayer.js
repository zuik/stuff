import React, {Component} from 'react';

class AudioTag extends Component {
    render() {
        return (<audio
            controls='controls'
            src={this.props.src}>
            Audio tag is not supported.
        </audio>);
    }
}

class Playlist extends Component {
    render() {
        return (<div>
            This is the playlist to be implement
        </div>)
    }
}

class AudioPlayer extends Component {
    render() {
        return (<div>
            <Playlist />
            <AudioTag src={this.props.src}/>
        </div>)
    }
}

export default AudioPlayer;

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
    constructor(props){
        super(props);
        this.playlistItems = this.props.tracks.map(
            (val, index) => <PlaylistItem changeSong={this.props.changeSong} key={index} name={val.name} url={val.url} />
        );

    }
    render() {
        return (<div>
            <ul>{this.playlistItems}</ul>
        </div>);
    }
}
// Todo: Change PlaylistItem to card style
class PlaylistItem extends Component {
    constructor(props){
        super(props);
        this.handlePlaylistItemClick = this.handlePlaylistItemClick.bind(this);
    }

    handlePlaylistItemClick (e) {
        e.preventDefault();
        console.log(e);
        console.log(this.props);
        this.props.changeSong(this.props.url);
    }

    render() {
        return (
        <li>
            <a href="#" onClick={this.handlePlaylistItemClick}> 
                    {this.props.name} | {this.props.url}
            </a>
        </li>);
    }
}

class AudioPlayer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            'src': '#',
            'tracks': [
                    {
                        'name': 'Blah blah',
                        'url': 'test.mp3'
                    },
                    {'name': 'Blah blah',
                        'url': 'b'
                    }
            ]
        };
        // Tracks need to be fetch from API and put in accordingly.
        this.changeSong = this.changeSong.bind(this);
    }
    changeSong (url) {
        this.setState({
            'src': url
        });
    }
    render() {
        return (<div>
            <Playlist changeSong={this.changeSong} tracks={this.state.tracks}/>
            <AudioTag src={this.state.src}/>
        </div>);
    }
}

export default AudioPlayer;

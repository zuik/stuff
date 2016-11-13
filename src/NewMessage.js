import React from 'react';
import TextField from 'material-ui/TextField';
import './css/main.css';

var serverUrl = "https://nearby-zkn.c9users.io/msg"


class NewMessage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            "text": "",
            "location": {
                "lat":null,
                "lng":null,
            },
            "username": "",
            "uid": "",
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
    }

    componentDidMount() {
        var _this = this;
        navigator.geolocation.getCurrentPosition(function(pos){
            if (pos){
                _this.setState({
                    "location": {
                        "lat": pos.coords.latitude,
                        "lng": pos.coords.longitude,
                    }
                });
            }
        });
    }

    handleSubmit(event) {
        event.preventDefault();
        let _this = this;
        let text = this.state.text;
        if (this.props.user){
            var user = {
                "username": this.props.user.displayName,
                "uid": this.props.user.uid,
                "profilePic": this.props.user.photoURL,
            };
        }
        console.log(this.props.user);
        fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'text': text,
                "location": {
                    "lat": _this.state.location.lat,
                    "lng": _this.state.location.lng,
                },
                "user": user,
            })
        }).then(function (resp) {
            _this.setState({"text": ""});
            _this.props.forceRerender();
        });

    }

    handleInputChange(event) {
        this.setState({
            "text": event.target.value
        });
    }

    render() {
        return (<form onSubmit={this.handleSubmit} style={{flex: 1}}>
            <TextField placeholder="Type a message!" value={this.state.text} onChange={this.handleInputChange} className="message-box"/>
        </form>);
    }
}

export default NewMessage;
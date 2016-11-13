import React from 'react';
import {List, ListItem} from 'material-ui/List';
import MapsPlace from 'material-ui/svg-icons/maps/place';
import moment from 'moment';
import NewMessage from './NewMessage';

var serverUrl = "https://nearby-zkn.c9users.io/msg"


class Messages extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            "messages": [{
                "content": []
            }],
        };
        this.getMessages = this.getMessages.bind(this);
        this.forceRerender = this.forceRerender.bind(this);
    }

    componentDidMount() {
        this.getMessages();
       // setInterval(this.getMessages, 5000);
    }

    getMessages() {
        var _this = this;
        fetch(serverUrl).then(function (resp) {
            return resp.json();
        }).then(function (j) {
            _this.setState({
                "messages": j['messages']
            });
        });
    }

    forceRerender() {
        this.getMessages();
    }

    render() {
        return <div><NewMessage forceRerender={this.forceRerender} user={this.props.user}/>
            {this.state["messages"].map(function (val) {
                var lat;
                var lng;
                var username;
                if (val.location){
                    lat = val.location.lat;
                    lng = val.location.lng;
                }
                if (val.user){
                    username = val.user.username
                }
                return <Message lat={lat} lng={lng} time={val.time} message={val.content} username={username}/>;
            })}
            
        </div>;
    }
}


class Message extends React.Component {
    render() {
        var time = this.props.time;
        time = moment.unix(time);
        time = time.format("MMM d, YYYY H:m:s");

        return <ListItem rightIcon={<a href={"https://www.google.com/maps?q=" + this.props.lat + ',' + this.props.lng }><MapsPlace /></a>} primaryText={this.props.message} secondaryText={<div> by <b>{this.props.username}</b> on <i>{time}</i></div>} />;
    }
}

export default Messages;
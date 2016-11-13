import React from 'react';
import AppBar from 'material-ui/AppBar';
import Login from './Login';
import Messages from './Messages';

class Main extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            "user": null
        }
        this.updateUserInfo = this.updateUserInfo.bind(this);
    }
    
    updateUserInfo(user) {
        this.setState({
            "user": user
        });
    }

    render() {
        return (<div>
            <AppBar title="A simple chat app that took way to long to do" iconElementRight={<Login updateHandler={this.updateUserInfo}/>}/>
            <Messages user={this.state.user}/>
        </div>);
    }
}

export default Main;
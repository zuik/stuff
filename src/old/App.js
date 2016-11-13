import React from 'react';
import './App.css';
import {Col, Button, ButtonToolbar} from 'react-bootstrap';
import moment from 'moment';
import './platform.js';
import AuthService from './auth/AuthService.js'


class Message extends React.Component {
    render() {
        var time = this.props.time;
        time = moment.unix(time);
        time = time.format("MMM d, YYYY H:m:s");
        return <div>
        <ul>
        <li>Time: {time}</li>
        <li>Message: {this.props.message}</li>
        </ul>
        </div>;
    }
}

class Login extends React.Component {
  render() {
    const { auth } = this.props
    return (
      <div>
        <h2>Login</h2>
        <ButtonToolbar>
          <Button bsStyle="primary" onClick={auth.login.bind(this)}>Login</Button>
        </ButtonToolbar>
      </div>
    )
  }
}

class Messager extends React.Component {
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
    }

    getMessages() {
        var _this = this;
        fetch("http://localhost:5000/msg").then(function (resp) {
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
        return <div>
        <Poster forceRerender={this.forceRerender}/>
            {this.state["messages"].map(function (val) {
                return <Message time={val.time} message={val.content}/>;
            })}
            
        </div>;
    }
}

class Poster extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            "text": ""
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        let _this = this;
        let text = this.state.text;

        fetch('http://localhost:5000/msg', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'text': text
            })
        }).then(function (resp) {
            _this.props.forceRerender();
        });

    }

    handleInputChange(event) {
        this.setState({
            "text": event.target.value
        });
    }

    render() {
        return (<form onSubmit={this.handleSubmit}>
            <input placeholder="Type a message!" value={this.state.text} onChange={this.handleInputChange}></input>
        </form>);
    }
}

class App extends React.Component{
  render() {
    return <Col md={6} mdPush={4}>
      <Login />
      <Messager />
    </Col>
  }
}

export default App;

import React from 'react';
import * as firebase from "firebase";
import FlatButton from 'material-ui/FlatButton';

var config = {
    apiKey: "AIzaSyCcdwSaeUisGBVLatMFwvtDJiFOkuEMbV8",
    authDomain: "universal-rider-149309.firebaseapp.com",
    databaseURL: "https://universal-rider-149309.firebaseio.com",
    storageBucket: "universal-rider-149309.appspot.com",
    messagingSenderId: "282294912427"
  };

firebase.initializeApp(config);

var provider = new firebase.auth.GoogleAuthProvider();

class Login extends React.Component{
    constructor(props) {
        super(props);
        this.handleLogin = this.handleLogin.bind(this);
        this.signout = this.signout.bind(this);
        this.state = {
            "user": firebase.auth().currentUser,
            "signnedIn":false
        }
        var _this = this;
        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                _this.setState({
                    "signnedIn": true,
                    "user": user
                });
                _this.props.updateHandler(user);
            } else {
                _this.setState({
                    "signnedIn": false
                });
            }
            });
    }

    handleLogin() {
        firebase.auth().signInWithPopup(provider).then(function(result) {
        // This gives you a Google Access Token. You can use it to access the Google API.
        var token = result.credential.accessToken;
        // The signed-in user info.
        var user = result.user;
        // ...
        }).catch(function(error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        // The email of the user's account used.
        var email = error.email;
        // The firebase.auth.AuthCredential type that was used.
        var credential = error.credential;
        // ...
        });
    }

    signout() {
        var _this = this;
        firebase.auth().signOut().then(function() {
            // Sign-out successful.
            _this.forceUpdate();
        }, function(error) {
        // An error happened.
        });
    }

    render() {
        if (!this.state.signnedIn){
            return <FlatButton label="Login"  onClick={this.handleLogin} />;
        } else {
            return <FlatButton label={this.state.user.displayName + ", signout?" } onClick={this.signout} />;
        }
    }
}

export default Login;
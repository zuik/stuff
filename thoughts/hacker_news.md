# Let's make a hacker news reader app!

Hacker News is great, however, its web interface is rather ... minimalistic. Couple with this minimalistic web interface, Hacker News also have a very simple API. Therefore, for beginners to web development (like me), making a Hacker News reader app seem like a right project to take up. 

Making Hacker News app isn't a new endavour, as there have been many attempts at making an interface for Hacker News. A simple web search could get you many. 

Our process to make a hacker news reader app will be in many step, each will iteratively add more feature to our app. 

## 1. Setup React

Assuming you have node and npm install, create an React app is as simple as `create-react-app [app-name]`.

If you don't have `create-react-app`, you could install it globally by `npm install -g create-react-app`. 

After the app is create, we could go into the app's directory and `npm start` or `yarn start` to see the default page for React App. 

## 2. Get data from Hacker News API

Let's take a look at the [Hacker News API](https://github.com/HackerNews/API).

First, our app should be able to display the top stories like we would see if we go on the main [Hacker News website](https://news.ycombinator.com). If we look at the `topstories` endpoint, we see that the API returns an array of 500 integers. Not very useful isn't it. 

Before thinking about what to do with getting actual information from this array of 500 integer, let's see how we can call this API endpoint and deliver the data into our React app.

```jsx
class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            hkns: []
        }
    }
    render() {
        let hkns = this.state.hkns.map((value, index) => {
            return (<li key={value}>{value}</li>);
        });
        return (<ul>{hkns}</ul>);
    }
}
```

Here, we iterate over the array of these 500 items and just making an unorder list out of them. However, our state is still empty. We need to make a network request to get those 500 items and update our state with it. 

```jsx
componentDidMount() {
    fetch("https://hacker-news.firebaseio.com/v0/topstories.json")
        .then(resp => resp.json())
        .then(json => {
            this.setState((prevState, props) => {
                return {hkns: json};
            });
        });

}
```


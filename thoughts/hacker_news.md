# Let's make a hacker news reader app!

Hacker News is great, however, its web interface is rather ... minimalistic. Couple with this minimalistic web interface, Hacker News also has a very simple API. Therefore, for a beginner to web development (like me), making a Hacker News reader app seem like a right project to take up. 

## 1. Setup React

Assuming you have node and npm install, create an React app is as simple as `create-react-app [app-name]`.

If you don't have `create-react-app`, you could install it globally by `npm install -g create-react-app`. 

After the app is created, we could go into the app's directory and `npm start` or `yarn start` to see the default page for React App. 

## 2. Get data from Hacker News API

Let's take a look at the [Hacker News API](https://github.com/HackerNews/API).

First, our app should be able to display the top stories like people would see if they go on the main [Hacker News website](https://news.ycombinator.com). If we look at the `topstories` endpoint, we see that the API returns an array of 500 integers. These are the IDs of the top 500 stories at the time.  

Before thinking about what to do with getting actual information from this array of 500 integer, let's see how we can call this API endpoint and deliver the data into our React app.

We can modify the `App` component directly.

```jsx
class App extends Component {
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

## 3. Finding data in a bunch of integer
So we have a bunch of number, great! Now we would have to look at getting individual items from the Hacker News API. 
Nicely, getting an item based on its ID is basically `https://hacker-news.firebaseio.com/v0/item/[item_id].json`. 

We can make a component that encapsulate an Hacker News story for us. First, we need to decide how to present this. Very crudely, we can put the data in a bunch of headings as follows.

```jsx
class HNStory extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: "-------",
            author: "----",
            url: "#",
        }
    }
    componentDidMount() {
        fetch(`https://hacker-news.firebaseio.com/v0/item/${this.props._id}.json`)
            .then(resp => resp.json())
            .then(json => {
                this.setState((prevState, props) => {
                    return {
                        title: json.title,
                        author: json.by,
                        url: json.url,
                    };
                })
            });
    }
    render(){
        return (<div className="hn-story">
            <h2><a href={this.state.url}>{this.state.title}</a></h2>
            <h3>by <i>{this.state.author}</i></h3>
        </div>);
    }
}
```

Before we can see anything, we have to modify the `render` function of our `App` container to renders these new `HNStory` containers. 

```jsx
 render() {
        let hkns = this.state.hkns.map((value, index) => {
            return (<li key={value}><HNStory _id={value} /></li>);
        });
        return (
            <div className="container">
                <ol>{hkns}</ol>
            </div>
        );
    }
```

And we successfully replicated the front page of Hacker News. Our version is even more minimalistic than the front page. 

Next, we will add more things into this minimal version of the app and hopefully make it better.
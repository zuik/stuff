# Semantics and Pragmatics
## Notes for the second midterm review
#### Duy Nguyen
#### The day before the exam

## Logic and Pragmatic Inference
### Shortfall of propositional logic
PropL is a very great thing. However, it does not mean that it's perfect. In particular, PropL has its shortcomming in describing the natural language. Observes these example:

**(3)**

    a. I didn't eat 3 (of the) cookies.
    
    b. I ate fewer than 3 cookies. 

    c. There are 3 cookies that I didn't eat. 

While PropL identify (3b) as ~r, it doesn't say anything meaningful about (3c). In particular, (3c) is a completely different topic in PropL's perspective, therefore the only way we can really represent it under the PropL is through a new variable. This is not I deal as we can see that all three sentences in (3) actually related to eachother. Both (3b) and (3c) are ways that people can understand an utterance of (3a).

**(4)**

    a. Johnny finished all of the cookies.

    b. Johnny finished some of the cookies. 

Even though there is entailment, PropL can't see the scalar relationship between **all** and **some**. Therefore, these two sentences are both assigned a different variable under the eyes of PropL.

**(5)**

    a. If N is an elephant, then N is a mamal. 

I actually have no idea what's wrong with this.

#### Therefore...
We see that these three shortfalls of PropL araised because fundamentally, PropL basic unit is a clause. We need something that have a smaller grasp on the elemement of language. In particular we need something that handles:

(5). The relativities between elephant and mamal (Categories).

(4). Terms like all, some, ... (Scalar)

(3). The interaction of **n't** and **3 cookies**. 

## Predicate Logic

To solve the problem of not being able to represent smaller element of the sentence, we have predicate logic. Instead of assignment variable to the sentence level meaning, we use small element of the sentence and make it a predicate.

We observes how English seperate the sentence:

|Subject|Predicate|
|--|--|
Rufus| is a **dog**.
Rufus| **barks**.
Rufus| is **large**.

We notes that the bolded words are where most of the meaning of the sentence actually is. In this case, these are DOG, BARK, and LARGE predicates respectively.

Beside its ability to takes arguments, predicates beheaves just like a variable in propositional logic.

### Predicates and their arguments
Predicates don't usually go alone. They usually takes arguments. The amount of arguments that they takes depends on their meaning. We can classify predicates on how many arguments they takes. Also, in writing, we define one letter lower case variable for the argument.

#### One place predicates
These one place predicates are usually terms that describes something or trying to put something in category. For example, LARGE, DOG, STUDENT, etc. 

|Sentence|PredL|
|--|--|
|Rufus is a dog.|DOG(r)|
|Alice is a student.|STUDENT(a)|
|Barney is sad.|SAD(b)|

#### Two places predicates
Two places predicate are usually verb. In particular, they are the sub-category of verb call *transitive verbs*. 

|Sentence|PredL|
|--|--|
|Anna talks to John|TALK(a, j)
|France is near England|NEAR(f, e)

#### Three and more places predicates
The more places a predicate has, the harder to find them. Three places predicates are usually what we called *ditransitive verbs*. These are verbs that take one subject, and two object, a direct object and an indirect object. The canonical example of this is the verb **give**. The predicate GIVE(a,b,c) is translated as *a gives b to c*.

Interestingly, there is also a preposition that takes three arguments. It is **in between**.

Four places predicates are very rare. One example is:
***Edinburgh** is closer to **Glasgow** than **Paris** is to **London***


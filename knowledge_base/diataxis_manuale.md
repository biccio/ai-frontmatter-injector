# Diátaxis

## A systematic approach to technical documentation authoring.

Diátaxis is a way of thinking about and doing documentation. It prescribes approaches to content, architecture and form that emerge from a systematic approach to understanding the needs of documentation users. Diátaxis identifies four distinct needs, and four corresponding forms of documentation - *tutorials*, *how-to guides*, *technical reference* and *explanation*. It places them in a systematic relationship, and proposes that documentation should itself be organised around the structures of those needs.

> *Diátaxis*, from the Ancient Greek δῐᾰ́τᾰξῐς: *dia* ("across") and *taxis* ("arrangement").

## Diátaxis solves problems related to documentation *content* (what to write), *style* (how to write it) and *architecture* (how to organise it). As well as serving the users of documentation, Diátaxis has value for documentation creators and maintainers. It is light-weight, easy to grasp and straightforward to apply. It doesn't impose implementation constraints. It brings an active principle of quality to documentation that helps maintainers think effectively about their own work.

Diátaxis is proven in practice. Its principles have been adopted successfully in hundreds of documentation projects.

> Diátaxis has allowed us to build a high-quality set of internal documentation that our users love, and our contributors love adding to.
> \-- Greg Frileux, `Vonage`

> At Gatsby we recently reorganized our open-source documentation, and the Diátaxis framework was our go-to resource
> throughout the project. The four quadrants helped us prioritize the user’s goal for each type of documentation. By
> restructuring our documentation around the Diátaxis framework, we made it easier for users to discover the
> resources that they need when they need them.
> \-- Megan Sullivan

> While redesigning the `Cloudflare developer docs`, Diátaxis became our north star for information architecture. When we weren't sure where a new piece of content should fit in, we'd consult the framework. Our documentation is now clearer than it's ever been, both for readers and contributors.
> \-- Adam Schwartz

-----

# Foundations

Diátaxis is successful because it *works* - both users and creators have a better experience of documentation as a result. It makes sense and it feels right.

However, that's not enough to be confident in Diátaxis as a theory of documentation. As a theory, it needs to show *why* it works. It needs to show that there is actually some reason why there are exactly four kinds of documentation, not three or five. It needs to demonstrate rigorous thinking and analysis, and that it stands on a sound theoretical foundation. Otherwise, it will be just another useful heuristic approach, and the strongest claim we can make for it is that "it seems to work quite well".

## Two dimensions of craft

Diátaxis is based on the principle that documentation must serve the needs of its users. Knowing how to do that means understanding what the needs of users are. The user whose needs Diátaxis serves is *the practitioner in a domain of skill*. A domain of skill is defined by a craft - the use of a tool or product is a craft. So is an entire discipline or profession. Using a programming language is a craft, as is flying a particular aircraft, or even being a pilot in general.

Understanding the needs of these users means in turn understanding the essential characteristics of craft or skill.

### Action/cognition

A skill or craft or practice contains both **action** (practical knowledge, knowing *how*, what we do) and **cognition** (theoretical knowledge, knowing *that*, what we think). The two are completely bound up with each other, but they are counterparts, wholly distinct from each, two different aspects of the same thing.

### Acquisition/application

Similarly, the relationship of a practitioner with their practice is that it is something that needs to be both **acquired**, and **applied**. Being "at work" (concerned with applying the skill and knowledge of their craft) and being "at study" (concerned with acquiring them) are once again counterparts, distinct but bound up with each other.

### The map of the territory

This gives us two dimensions of skill, that we can lay out on a map - a map of the territory of craft.

This is a *complete* map. There are only two dimensions, and they don't just cover the entire territory, they define it. This is why there are necessarily four quarters to it, and there could not be three, or five. It is not an arbitrary number.

It also shows us the *qualities* of craft that define each of them. When the idea that documentation must serve the needs of craft is applied to this map, it reveals in turn what documentation must be and do to fulfil those obligations - in four distinct ways.

## Serving needs

The map of the territory of craft is what gives us the familiar Diátaxis map of documentation. The map is in effect an answer to the question: what must documentation do to align with these qualities of skill, and to what need is it oriented in each case?.

We can see how the map of documentation addresses *needs* across those two dimensions, each need also defined by the characteristics of its quarter of the map.

| need | addressed in | the user | the documentation |
| :--- | :--- | :--- | :--- |
| learning | tutorials | acquires their craft | informs action |
| goals | how-to guides | applies their craft | informs action |
| information | reference | applies their craft | informs cognition |
| understanding | explanation | acquires their craft | informs cognition |

The Diátaxis map of documentation is a memorable and approachable idea. But, a map is only reliable if it adequately describes a reality. Diátaxis is underpinned by a systematic description and analysis of generalised **user needs**. This is why the tutorials, how-to guides, reference and explanation of Diátaxis are a complete enumeration of the types of documentation that serve practitioners in a craft. This is why there are four and only four types of documentation. There is simply no other territory to cover.

-----

# The map

One reason Diátaxis is effective as a guide to organising documentation is that it describes a **two-dimensional structure**, rather than a *list*.

It specifies its types of documentation in such a way that the structure naturally helps guide and shape the material it contains. As a map, it places the different forms of documentation into relationships with each other. Each one occupies a space in the mental territory it outlines, and the boundaries between them highlight their distinctions.

## The problem of structure

When documentation fails to attain a good structure, it's rarely just a problem of structure (though it's bad enough that it makes it harder to use and maintain). Architectural faults infect and undermine content too.

In the absence of a clear, generalised documentation architecture, documentation creators will often try to structure their work around features of a product. This is rarely successful, even in a single instance. In a portfolio of documentation instances, the results are wild inconsistency. Much better is the adoption of a scheme that tries to provide an answer to the question: how to arrange documentation *in general?*.

In fact any orderly attempt to organise documentation into clear content categories will help improve it (for authors as well as users), by providing lists of content types. Even so, authors often find themselves needing to write particular documentation content that fails to fit well within the categories put forward by a scheme, or struggling to rewrite existing material. Often, there is a sense of arbitrariness about the structure that they find themselves working with - why this particular list of content types rather than another?. And if another competing list is proposed, which to adopt?.

## Expectations and guidance

A clear advantage of organising material this way is that it provides both clear *expectations* (to the reader) and *guidance* (to the author). It's clear what the purpose of any particular piece of content is, it specifies how it should be written and it shows where it should be placed.

| | Tutorials | How-to guides | Reference | Explanation |
| :--- | :--- | :--- | :--- | :--- |
| **what they do** | introduce, educate, lead | guide | state, describe, inform | explain, clarify, discuss |
| **answers the question** | "Can you teach me to...?"  | "How do I...?"  | "What is...?"  | "Why...?"  |
| **oriented to** | learning  | goals  | information  | understanding  |
| **purpose** | to provide a learning experience | to help achieve a particular goal | to describe the machinery | to illuminate a topic |
| **form** | a lesson | a series of steps | dry description | discursive explanation  |
| **analogy** | teaching a child how to cook | a recipe in a cookery book | information on the back of a food packet | an article on culinary social history |

Each piece of content is of a kind that not only has one particular job to do, that job is also clearly distinguished from and contrasted with the other functions of documentation.

## Blur

Most documentation systems and authors recognise at least some of these distinctions and try to observe them in practice.

However, there is a kind of natural affinity between each of the different forms of documentation and its neighbours on the map, and a natural tendency to blur the distinctions (that can be seen repeatedly in examples of documentation).

| | | |
| :--- | :--- | :--- |
| **guide action** | tutorials | how-to guides |
| **serve the application of skill**| reference | how-to guides |
| **contain propositional knowledge**| reference | explanation |
| **serve the acquisition of skill**| tutorials | explanation |

When these distinctions are allowed to blur, the different kinds of documentation bleed into each other. Writing style and content make their way into inappropriate places. It also causes structural problems, which make it even more difficult to maintain the discipline of appropriate writing.

In the worst case there is a complete or partial collapse of tutorials and how-to guides into each other, making it impossible to meet the needs served by either.

-----

## The journey around the map

Diátaxis is intended to help documentation better serve users in their *cycle of interaction* with a product. This phrase should not be understood too literally. It is not the case that a user must encounter the different kinds of documentation in the order *tutorials* \> *how-to guides* \> *technical reference* \> *explanation*. In practice, an actual user may enter the documentation anywhere in search of guidance on some particular subject, and what they want to read will change from moment to moment as they use your documentation.

However, the idea of a cycle of documentation needs, that proceeds through different phases, is sound and corresponds to the way that people actually do become expert in a craft. There is a sense and meaning to this ordering.

  * ***learning-oriented phase***: We begin by learning, and learning a skill means diving straight in to do it - under the guidance of a teacher, if we're lucky.
  * ***goal-oriented phase***: Next we want to put the skill to work.
  * ***information-oriented phase***: As soon as our work calls upon knowledge that we don't already have in our head, it requires us to consult technical reference.
  * ***explanation-oriented phase***: Finally, away from the work, we reflect on our practice and knowledge to understand the whole.

And then it's back to the beginning, perhaps for a new thing to grasp, or to penetrate deeper.

-----

# The compass

The Diátaxis map is an effective reminder of the different kinds of documentation and their relationship, and it accords well with intuitions about documentation. However intuition is not always to be relied upon. Often when working with documentation, an author is faced with the question: *what form of documentation is this?* or *what form of documentation is needed here?* - and no obvious, intuitive answer. Worse, sometimes intuition provides an immediate answer that is also wrong.

A map is most powerful in unfamiliar territory when we also have a compass to guide us. The Diátaxis compass is something like a truth-table or decision-tree of documentation. It reduces a more complex, two-dimensional problem to its simpler parts, and provides the author with a course-correction tool.

| If the content... | ...and serves the user's... | ...then it must belong to... |
| :--- | :--- | :--- |
| informs action | acquisition of skill | a tutorial |
| informs action | application of skill | a how-to guide |
| informs cognition | application of skill  | reference |
| informs cognition | acquisition of skill | explanation |

The compass can be applied equally to user situations that need documentation, or to documentation itself that perhaps needs to be moved or improved. Like many good tools, it's surprisingly banal.

To use the compass, just two questions need to be asked: *action or cognition?* *acquisition or application?*

And it yields the answer.

## Using the compass

The compass is particularly effective when you think that you think you (or even the documentation in front of you) are doing one thing - but you are troubled by a sense of doubt, or by some difficulty in the work. The compass forces you to stop and reconsider.

Especially when you are trying to find your initial bearings, use the compass's terms flexibly; don't get fixated on the exact names.

  * ***action***: practical steps, doing
  * ***cognition***: theoretical or propositional knowledge, thinking
  * ***acquisition***: study
  * ***application***: work

And the questions themselves can also be used in different ways:

  * Do I think I am writing for *x* or *y*? 
  * Is this writing in front of me engaged in *x* or *y*? 
  * Does the user need *x* or *y*?
  * Do I want to *x* or *y*? 

And try applying them close-up, at the level of sentences and words, or from a wider perspective, considering an entire document.

-----

# Applying Diátaxis

The pages in this section are concerned with putting Diátaxis into practice.

> Diátaxis is underpinned by :doc:`systematic theoretical principles <theory>`, but understanding them is not necessary to make effective use of the system.

Diátaxis is primarily intended as a pragmatic approach for people working on documentation. Most of the key principles required to put it into practice successfully can be grasped intuitively.

## Don't wait to understand Diátaxis before you start trying to put it into practice. Not only do you not need to understand it all to make use of it, you will not understand it until you have started using it (this itself is a Diátaxis principle). As soon as you feel you have picked up an idea that seems worth applying to your work, try applying it. Come back here when you need more clarity or reassurance. Iterate between your work and reflecting on your work.

## In this section

At the core of Diátaxis are the four different kinds of documentation it identifies. If you're encountering Diátaxis for the first time, start with these pages.

  * :doc:`tutorials` - learning-oriented experiences
  * :doc:`how-to-guides` - goal-oriented directions
  * :doc:`reference` - information-oriented technical description
  * :doc:`explanation` - understanding-oriented discussion

Diátaxis prescribes principles that guide action. These translate into particular ways of working, with implications for documentation process and execution. Once you've made your first start, the tools and methods outlined here will help smooth your way.

  * :doc:`compass` - a simple tool for direction-finding
  * :doc:`Workflow <how-to-use-diataxis>` in Diátaxis

-----

# How-to guides

How-to guides are **directions** that guide the reader through a problem or towards a result. How-to guides are **goal-oriented**.

\===========

A how-to guide helps the user get something done, correctly and safely; it guides the user's *action*.

It's concerned with *work* - navigating from one side to the other of a real-world problem-field.

Examples could be: *how to calibrate the radar array*; *how to use fixtures in pytest*; *how to configure reconnection back-off policies*. On the other hand, *how to build a web application* is not - that's not addressing a specific goal or problem, it's a vastly open-ended sphere of skill.

# How-to guides matter not just because users need to be able to accomplish things: the list of how-to guides in your documentation helps frame the picture of what your product can actually *do*. A rich list of how-to guides is an encouraging suggestion of a product's capabilities. Well-written how-to guides that address the right questions are likely to be the most-read sections of your documentation.

## How-to guides addressed to problems

**How-to guides must be written from the perspective of the user, not of the machinery.** A how-to guide represents something that someone needs to get done. It's defined in other words by the needs of a user. Every how-to guide should answer to a human project, in other words. It should show what the human needs to do, with the tools at hand, to obtain the result they need.

This is in strong contrast to common pattern for how-to guides that often prevails, in which how-to guides are defined by operations that can be performed with a tool or system. The problem with this latter pattern is that it offers little value to the user; it is not addressed to any need the user has. Instead, it's focused on the tool, on taking the machinery through its motions.

This is fundamentally a distinction of *meaningfulness*. Meaning is given by purpose and need. There is no purpose or need in the functionality of a machine. It is merely a series of causes and effects, inputs and outputs.

Consider:

  * "To shut off the flow of water, turn the tap clockwise." 
  * "To deploy the desired database configuration, select the appropriate options and press **Deploy**." 

> We really do not need to be informed that we turn on a device using the power switch, but it is shocking how often how-to guides in software documentation are written at this level.

The examples above *look* like examples of guidance, but they are not. They represent mostly useless information that anyone with basic competence - anyone who is working in this domain - should be expected to know. Between them, standardised interfaces and generally-expected knowledge should make it quite clear what effect most actions will have.

Secondly, they are disconnected from purpose. What the user needs to know might be things like:

  * how much water to run, and how vigorously to run it, for a certain purpose
  * what database configuration options align with particular real-world needs

> How-to guides are about goals, projects and problems, not about tools.

# Tools appear in how-to guides as incidental bit-players, the means to the user's end. Sometimes of course, a particular end is closely aligned with a particular tool or part of the system, and then you will find that a how-to guide indeed concentrates on that. Just as often, a how-to guide will cut across different tools or parts of a system, joining them up together in a series of activities defined by something a human being needs to get done. In either case, it is that project that defines what a how-to guide must cover.

## What how-to guides are not

**How-to guides are wholly distinct from tutorials**. They are often confused, but the user needs that they serve are quite different. Conflating them is at the root of many difficulties that afflict documentation. See :ref:`tutorials-how-to` for a discussion of this distinction.

# In another confusion, how-to guides are often construed merely as procedural guides. But solving a problem or accomplishing a task cannot always be reduced to a procedure. Real-world problems do not always offer themselves up to linear solutions. The sequences of action in a how-to guide sometimes need to fork and overlap, and they have multiple entry and exit-points. Often, a how-to guide will need the user to rely on their judgement in applying the guidance it can provide.

## Key principles

A how to-guide is concerned with work - a task or problem, with a practical goal. *Maintain focus on that goal*.

> **How-to characteristics**
>
>   * focused on tasks or problems
>   * assume the user knows what they want to achieve
>   * action and only action
>   * no digression, explanation, teaching

Anything else that's added distracts both you and the user and dilutes the useful power of the guide. Typically, the temptations are to explain or to provide reference for completeness. Neither of these are part of guiding the user in their work. They get in the way of the action; if they're important, link to them.

A how-to guide serves the work of the already-competent user, whom you can assume to know what they want to do, and to be able to follow your instructions correctly.

### Address real-world complexity

**A how-to guide needs to be adaptable to real-world use-cases**. One that is useless for any purpose except *exactly* the narrow one you have addressed is rarely valuable. You can't address every possible case, so you must find ways to remain open to the range of possibilities, in such a way that the user can adapt your guidance to their needs.

### Omit the unnecessary

In how-to guides, **practical usability is more helpful than completeness.** Whereas a tutorial needs to be a complete, end-to-end guide, a how-to guide does not. It should start and end in some reasonable, meaningful place, and require the reader to join it up to their own work.

### Provide a set of instructions

A how-to guide describes an *executable solution* to a real-world problem or task. It's in the form of a contract: if you're facing this situation, then you can work your way through it by taking the steps outlined in this approach. The steps are in the form of *actions*.

"Actions" in this context includes physical acts, but also thinking and judgement - solving a problem involves thinking it through. A how-to guide should address how the user thinks as well as what the user does.

### Describe a logical sequence

The fundamental structure of a how-to guide is a *sequence*. It implies logical ordering in time, that there is a sense and meaning to this particular order. In many cases, the ordering is simply imposed by the way things must be (step two requires completion of step one, for example). In this case it's obvious what order your directions should take.

Sometimes the need is more subtle - it might be possible to *perform* two operations in either order, but if for example one operation helps set up the user's working environment or even their thinking in a way that benefits the other, that's a good reason for putting it first.

### Seek flow

At all times, try to ground your sequences in the patterns of the *user's* activities and thinking, in such a way that the guide acquires *flow*: smooth progress.

Achieving flow means successfully understanding the user. Paying attention to sense and meaning in ordering requires paying attention to the way human beings think and act, and the needs of someone following directions. Again, this can be somewhat obvious: a workflow that has the user repeatedly switching between contexts and tools is clearly clumsy and inefficient.

But you should look more deeply than this. What are you asking the user to think about, and how will their thinking flow from subject to subject during their work?. How long do you require the user to hold thoughts open before they can be resolved in action?. If you require the user to jump back to earlier concerns, is this necessary or avoidable?.

A how-to guide is concerned not just with logical ordering in time, but action taking place in time. Action, and a guide to it, has pace and rhythm. Badly-judged pace or disrupted rhythm are both damaging to flow.

At its best, how-to documentation gives the user flow. There is a distinct experience of encountering a guide that appears to *anticipate* the user - the documentation equivalent of a helper who has the tool you were about to reach for, ready to place it in your hand.

### Pay attention to naming

**Choose titles that say exactly what a how-to guide shows.**

  * good: *How to integrate application performance monitoring*
  * bad: *Integrating application performance monitoring* (maybe the document is about how to decide whether you should, not about how to do it)
  * very bad: *Application performance monitoring* (maybe it's about *how* - but maybe it's about *whether*, or even just an explanation of *what* it is)

# Note that search engines appreciate good titles just as much as humans do.

## The language of how-to guides

*This guide shows you how to...*

> Describe clearly the problem or task that the guide shows the user how to solve.

*If you want x, do y. To achieve w, do z.*

> Use conditional imperatives.

*Refer to the x reference guide for a full list of options.*

> Don't pollute your practical how-to guide with every possible thing the user might do related to x.

\================

## Applied to food and cooking

Consider a recipe, an excellent model for a how-to guide. A recipe clearly defines what will be achieved by following it, and **addresses a specific question** (*How do I make...?* or *What can I make with...?*).

It's not the responsibility of a recipe to *teach* you how to make something. A professional chef who has made exactly the same thing multiple times before may still follow a recipe - even if they *created* the recipe themselves - to ensure that they do it correctly.

Even following a recipe **requires at least basic competence**. Someone who has never cooked before should not be expected to follow a recipe with success, so a recipe is not a substitute for a cooking lesson. Someone who expected to be provided with a recipe, and is given instead a cooking lesson, will be disappointed and annoyed.

Similarly, while it's interesting to read about the context or history of a particular dish, the one time you don't want to be faced with that is while you are in the middle of trying to make it. A good recipe follows a well-established format, that excludes both teaching and discussion, and focuses only on **how** to make the dish concerned.

-----

# Explanation

Explanation is a discursive treatment of a subject, that permits *reflection*. Explanation is **understanding-oriented**.

\===========

Explanation deepens and broadens the reader's understanding of a subject. It brings clarity, light and context.

The concept of *reflection* is important. Reflection occurs *after* something else, and depends on something else, yet at the same time brings something new - shines a new light - on the subject matter.

The perspective of explanation is higher and wider than that of the other three types. It does not take the user's eye-level view, as in a how-to guide, or a close-up view of the machinery, like reference material. Its scope in each case is a topic - "an area of knowledge", that somehow has to be bounded in a reasonable, meaningful way.

For the user, explanation joins things together. It's an answer to the question: *Can you tell me about ...?*.

# It's documentation that it makes sense to read while away from the product itself (one could say, explanation is the only kind of documentation that it might make sense to read in the bath).

## The value and place of explanation

### Explanation and understanding

Explanation is characterised by its distance from the active concerns of the practitioner. It doesn't have direct implications for what they do, or for their work. This means that it's sometimes seen as being of lesser importance. That's a mistake; it may be less *urgent* than the other three, but it's no less *important*. It's not a luxury.

No practitioner of a craft can afford to be without an understanding of that craft, and needs the explanatory material that will help weave it together.

> **Explanation by any other name**
>
> Your explanation documentation doesn't need to be called *Explanation*. Alternatives include:
>
>   * *Discussion*
>   * *Background*
>   * *Conceptual guides*
>   * *Topics*

The word *explanation* - and its cognates in other languages - refer to *unfolding*, the revelation of what is hidden in the folds. So explanation brings to the light things that were implicit or obscured.

Similarly, words that mean *understanding* share roots in words meaning to hold or grasp (as in *comprehend*). That's an important part of understanding, to be able to hold something or be in possession of it.

Understanding seals together the other components of our mastery of a craft, and makes it safely our own. Understanding doesn't *come from* explanation, but explanation is required to form that web that helps hold everything together. Without it, the practitioner's knowledge of their craft is loose and fragmented and fragile, and their exercise of it is *anxious*.

### Explanation and its boundaries

Quite often explanation is not explicitly recognised in documentation; and the idea that things need to be explained is often only faintly expressed. Instead, explanation tends to be scattered in small parcels in other sections.

It's not always easy to write good explanatory material. Where does one start?. It's also not clear where to conclude. There is an open-endedness about it that can give the writer too many possibilities.

Tutorials, how-to-guides and reference are all clearly defined in their scope by something that is also well-defined: by what you need the user to learn, what task the user needs to achieve, or just by the scope of the machine itself.

# In the case of explanation, it's useful to have a real or imagined *why* question to serve as a prompt. Otherwise, you simply have to draw some lines that mark out a reasonable area and be satisfied with that.

## Writing good explanation

### Make connections

When writing explanation you are helping to weave a web of understanding for your readers. **Make connections** to other things, even to things outside the immediate topic, if that helps.

### Provide context

**Provide background and context in your explanation**: explain *why* things are so - design decisions, historical reasons, technical constraints - draw implications, mention specific examples.

### Talk *about* the subject

> **Things to discuss**
>
>   * the bigger picture
>   * history
>   * choices, alternatives, possibilities
>   * why: reasons and justifications

Explanation guides are *about* a topic in the sense that they are *around* it. Even the names of your explanation guides should reflect this; you should be able to place an implicit (or even explicit) *about* in front of each title. For example: *About user authentication*, or *About database connection policies*.

### Admit opinion and perspective

Opinion might seem like a funny thing to introduce into documentation. The fact is that all human activity and knowledge is invested within opinion, with beliefs and thoughts. The reality of any human creation is rich with opinion, and that needs to be part of any understanding of it.

Similarly, any understanding comes from a perspective, a particular stand-point - which means that other perspectives and stand-points exist. **Explanation can and must consider alternatives**, counter-examples or multiple different approaches to the same question. In explanation, you're not giving instruction or describing facts - you're opening up the topic for consideration. It helps to think of explanation as discussion: discussions can even consider and weigh up contrary *opinions*.

### Keep explanation closely bounded

# One risk of explanation is that it tends to absorb other things. The writer, intent on covering the topic, feels the urge to include instruction or technical description related to it. But documentation already has other places for these, and allowing them to creep in interferes with the explanation itself, and removes them from view in the correct place.

## The language of explanation

*The reason for x is because historically, y ...*

> Explain.

*W is better than z, because ...*

> Offer judgements and even opinions where appropriate..

*An x in system y is analogous to a w in system z. However ...*

> Provide context that helps the reader.

*Some users prefer w (because z). This can be a good approach, but...*

> Weigh up alternatives.

*An x interacts with a y as follows: ...*

> Unfold the machinery's internal secrets, to help understand why something does what it does.

\================

## Analogy from food and cooking

In 1984 `Harold McGee` published *On food and cooking*.

The book doesn't teach how to cook anything. It doesn't contain recipes (except as historical examples) and it isn't a work of reference. Instead, it places food and cooking in the context of history, society, science and technology. It explains for example why we do what we do in the kitchen and how that has changed.

It's clearly not a book we would read *while* cooking. We would read when we want to reflect on cooking. It illuminates the subject by taking multiple different perspectives on it, shining light from different angles.

After reading a book like *On food and cooking*, our understanding is changed. Our knowledge is richer and deeper. What we have learned may or may not be immediately applicable next time we are doing something in the kitchen, but *it will change how we think about our craft, and will affect our practice*.

-----

# Diátaxis as a guide to work

As well as providing a guide to documentation content, Diátaxis is also a guide to documentation process and execution.

Most people who work on technical documentation must make decisions about how to work, as they work. In some contexts, documentation must be delivered once, complete and in its final state, but it's more usual that it's an on-going project, for example developed alongside a product that itself evolves and develops.

It's also the experience of many people who work on documentation to find themselves responsible for improving or even remediating a body of work.

Diátaxis provides an approach to work that runs counter to much of the accepted wisdom in documentation. In particular, it discourages planning and top-down workflows, preferring instead small, responsive iterations from which overall patterns emerge.

## Use Diátaxis as a guide, not a plan

Diátaxis describes a complete picture of documentation. However the structure it proposes is not intended to be a **plan**, something you must complete in your documentation. It's a **guide**, a map to help you check that you're in the right place and going in the right directions.

The point of Diátaxis is to give you a way to think about and understand your documentation, so that you can make better sense of what it's doing and what you're trying to do with it. It provides tools that help assess it, identify where its problems lie, and judge what you can do to improve it.

## Don't worry about structure

Although structure is key to documentation, **using Diátaxis means not spending energy trying to get its structure correct**. If you continue to follow the prompts that Diátaxis provides, eventually your documentation will assume the Diátaxis structure - but it will have assumed that shape *because* it has been improved. It's not the other way round, that the structure must be imposed upon documentation to improve it.

Getting started with Diátaxis does not require you to think about dividing up your documentation into four sections. **It certainly does not mean that you should create empty structures for tutorials/howto guides/reference/explanation with nothing in them.** Don't do that. It's horrible.

Instead, following the workflow described in the next two sections, make changes where you see opportunities for improvement according to Diátaxis principles, so that the documentation starts to take a certain shape. At a certain point, the changes you have made will appear to demand that you move material under a certain Diátaxis heading - and that is how your top-level structure will form. In other words, **Diátaxis changes the structure of your documentation from the inside**.

## Work one step at a time

Diátaxis strongly prescribes a structure, but whatever the state of your existing documentation - even if it's a complete mess by any standards - it's always possible to improve it, **iteratively**.

It's natural to want to complete large tranches of work before you publish them, so that you have something substantial to show each time. Avoid this temptation - every step in the right direction is worth publishing immediately.

Although Diátaxis is intended to provide a big picture of documentation, **don't try to work on the big picture**. It's both unnecessary and unhelpful. Diátaxis is designed to guide small steps; keep taking small steps to arrive where you want to go.

## Just do something

If you're tidying up a huge mess, the temptation is to tear it all down and start again. Again, avoid it. As far as improving documentation in-line with Diátaxis goes, it isn't necessary to seek out things to improve. Instead, the best way to apply Diátaxis is as follows:

**Choose something** - any piece of the documentation. If you don’t already have something that you know you want to put right, don't go looking for outstanding problems. Just look at what you have right in front of you at that moment: the file you’re in, the last page you read - it doesn’t matter. If there isn’t one just choose something, literally at random.

**Assess it**. Next consider this thing critically. Preferably it’s a small thing, nothing bigger than a page - or better, even smaller, a paragraph or a sentence. Challenge it, according to the standards Diátaxis prescribes: *What user need is represented by this? How well does it serve that need? What can be added, moved, removed or changed to serve that need better? Do its language and logic meet the requirements of this mode of documentation?* 

**Decide what to do**. Decide, based on your answers to those questions: *What single next action will produce an immediate improvement here?* 

**Do it**. Complete that next single action, *and consider it completed* - i.e. publish it, or at least commit the change. Don't feel that you need to do anything else to make a worthy improvement.

And then go back to the beginning of the cycle.

Working like this helps reduce the stress of one of the most paralysing and troublesome aspects of the documentation-writer's work: working out what to do. It keeps work flowing in the right direction, always towards the desired end, without having to expend energies on a plan.

## Allow your work to develop organically

There's a strong urge to work in a cycle of planning and execution in order to work towards results. But it's not the only way, and there are often better ways when working with documentation.

### Well-formed organic growth

A good model for documentation is **well-formed organic growth that adapts to external conditions**. Organic growth takes place at the cellular level. The structure of the organism as a whole is guaranteed by the healthy development of cells, according to rules that are appropriate to each kind of cell. It's not the other way round, that a structure is imposed on the organism from above or outside. Good structure develops from within.

It's the same with documentation: by following the principles that Diátaxis provides, your documentation will attain a healthy structure, because its internal components themselves are well-formed - like a living organism, it will have built itself up from the inside-out, one cell at a time.

### Complete, not finished

Consider a plant. As a living, growing organism, a plant is **never finished** - it can always develop further, move on to the next stage of growth and maturity. But, at every stage of its development, from seed to a fully-mature tree, it's **always complete** - there's never something missing from it. At any point, it is in a state that is appropriate to its stage of development.

Similarly, documentation is also never finished, because it always has to keep adapting and changing to the product and to users' needs, and can always be developed and improved further. However it can always be complete: useful to users, appropriate to its current stage of development, and in a healthy structural state and ready to go on to the next stage.

-----

# Diátaxis in complex hierarchies

## Structure of documentation content

The application of Diátaxis to most documentation is fairly straightforward. The product that defines the domain of concern has clear boundaries, and it's possible to come up with an arrangement of documentation contents that looks - for example - like this:

```text
Home                      <- landing page
    Tutorial              <- landing page
        Part 1
        Part 2
        Part 3
    How-to guides         <- landing page
        Install
        Deploy
        Scale
    Reference             <- landing page
        Command-line tool
        Available endpoints
        API
    Explanation           <- landing page
        Best practice recommendations
        Security overview
        Performance
```

In each case, a landing page contains an overview of the contents within. The tutorial for example describes what the tutorial has to offer, providing context for it.

### Adding a layer of hierarchy

Even very large documentation sets can use this effectively, though after a while some grouping of content within sections might be wise. This can be done by adding another layer of hierarchy - for example to be able to address different installation options separately:

```text
Home                      <- landing page
    Tutorial              <- landing page
        Part 1
        Part 2
        Part 3
    How-to guides         <- landing page
        Install           <- landing page
            Local installation
            Docker
            Virtual machine
            Linux container
        Deploy
        Scale
    Reference             <- landing page
        Command-line tool
        Available endpoints
        API
    Explanation           <- landing page
        Best practice recommendations
        Security overview
        Performance
```

## Contents pages

Contents pages - typically a home page and any landing pages - provide an overview of the material they encompass. There is an art to creating a good contents page. The experience they give the users deserves careful consideration.

### The problem of lists

Lists longer than a few items are very hard for humans to read, unless they have an inherent mechanical order - numerical, or alphabetical. *Seven items seems to be a comfortable general limit.* If you find that you're looking at lists longer than that in your tables of contents, you probably need to find a way to break them up into small ones.

As always, what matters most is **the experience of the reader**. Diátaxis works because it fits user needs well - if your execution of Diátaxis leads you to formats that seem uncomfortable or ugly, then you need to use it differently.

### Overviews and introductory text

**The content of a landing page itself should read like an overview.**

That is, it should not simply present lists of other content, it should introduce them. *Remember that you are always authoring for a human user, not fulfilling the demands of a scheme.*

Headings and snippets of introductory text catch the eye and provide context; for example, a **how-to landing page**:

```text
How to guides
=============

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Installation guides
-------------------

Pellentesque malesuada, ipsum ac mollis pellentesque, risus 
[cite_start]nunc ornare odio, et imperdiet dui mi et dui. Phasellus vel 
[cite_start]porta turpis. [cite_start]In feugiat ultricies ipsum.

* Local installation       |
* Docker                   | links to
* Virtual machines         | the guides
* Linux containers         |

Deployment and scaling
-----------------------

[cite_start]Morbi sed scelerisque ligula. In dictum lacus quis felis 
[cite_start]facilisisvulputate. Quisque lacinia condimentum ipsum 
[cite_start]laoreet tempus.

* Deploy an instance       | links to
* Scale your application   | the guides
```

## Two-dimensional problems

A more difficult problem is when the structure outlined by Diátaxis meets another structure - often, a structure of topic areas within the documentation, or when documentation encounters very different user-types.

For example we might have a product that is used on land, sea and air, and though the same product, is used quite differently in each case. And it could be that a user who uses it on land is very unlikely to use it at sea.

Or, the product documentation addresses the needs of:

  * users
  * developers who build other products around it
  * the contributors who help maintain it.

The same product, but very different concerns.

A final example: a product that can be deployed on different public clouds, with each public cloud presenting quite different workflows, commands, APIs, GUIs, constraints and so on. Even though it's the same product, as far as the users in each case are concerned, what they need to know and do is very different - what they need is documentation not for *product*, but

  * *product-on-public-cloud-one*
  * *product-on-public-cloud-two*
  * and so on...

So, we *could* decide on an overall structure that does this:

```text
tutorial
    for users on land
        [...]
    for users at sea
        [...]
    for users in the air
        [...]
[and then so on for how-to guides, reference and explanation]
```

or maybe instead this:

```text
for users on land
    tutorial
        [...]
    how-to guides
        [...]
    reference
        [...]
    explanation
        [...]
for users at sea
    [tutorial, how-to, reference, explanation sections]
for users in the air
    [tutorial, how-to, reference, explanation sections]
```

Which is better?. There seems to be a lot of repetition in either cases. What about the material that can be shared between land, sea and air?.

### What *is* the problem?

Firstly, the problem is in no way limited to Diátaxis - there would be the difficulty of managing documentation in any case. However, Diátaxis certainly helps reveal the problem, as it does in many cases. It brings it into focus and demands that it be addressed.

Secondly, the question highlights a common misunderstanding. Diátaxis is not a scheme into which documentation must be placed - four boxes. It posits four different kinds of documentation, around which documentation should be structured, but this does not mean that there must be simply four divisions of documentation in the hierarchy, one for each of those categories.

## Diátaxis as an approach

Diátaxis can be neatly represented in a diagram - but it is not the *same* as that diagram. It should be understood as an approach, a way of working with documentation, that identifies four different needs and uses them to author and structure documentation effectively. This will *tend* towards a clear, explicit, structural division into the four categories - but that is a typical outcome of the good practice, not its end.

## User-first thinking

**Diátaxis is underpinned by attention to user needs**, and once again it's that concern that must direct us.

What we must document is the product *as it is for the user*, the product as it is in their hands and minds. (Sadly for the creators of products, how they conceive them is much less relevant.) .

Is the product on land, sea and air effectively three different products, perhaps for three different users?. In that case, let that be the starting point for thinking about it.

If the documentation needs to meet the needs of users, developers and contributors, how do *they* see the product?. Should we assume that a developer who incorporates it into other products will typically need a good understanding of how it's used, and that a contributor needs to know what a developer knows too?. Then perhaps it makes sense to be freer with the structure, in some parts (say, the tutorial) allowing the developer-facing content to follow on from the user-facing material, while completely separating the contributors' how-to guides from both.

And so on. If the structure is not :ref:`the simple, uncomplicated structure we began with <basic-structure>`, that's not a problem - as long as there *is* arrangement according to Diátaxis principles, that documentation does not muddle up its different forms and purposes.

### Let documentation be complex if necessary

Documentation should be as complex as it needs to be. It will sometimes have complex structures. But, even complex structures can be made straightforward to navigate as long as they are logical and incorporate patterns that fit the needs of users.

-----

# Colophon

Diátaxis is the work of `Daniele Procida`.

It has been developed over a number of years, and continues to be elaborated and explored.

## Contact me

`Email me`. I enjoy hearing about other people's experiences with Diátaxis and read everything I receive. I appreciate all the interest and do my best to reply, but I get a considerable quantity of email related to Diátaxis and I can't promise to respond to every message.

If you'd like to discuss Diátaxis with other users, please see the *\#diataxis* channel on the `Write the Docs Slack group`, or the `Discussions` section of the `GitHub repository for this website`.

## Origins and development

You can find `an earlier presentation of some of these ideas`, that I created while working at Divio between 2014-2021. I still agree with most of it, though there are several aspects that I now think I got wrong.

The original context for the Diátaxis approach was limited to software product documentation. In 2021 I was awarded a Fellowship of the `Software Sustainability Institute`, to explore its application in scientific research contexts. More recently I've explored its application in internal corporate documentation, organisational management and education, and also its application at scale. This work is on-going.

Other people have corresponded with me to share their experience of applying Diátaxis to note-taking systems and even as part of a systematic approach to household management.

## Citation and contribution

To cite Diátaxis, please refer to :doc:`this website, diataxis.fr <index>`. The Git repository for the source material contains a citation file, `CITATION.cff`. APA and BibTeX metadata are available from the *Cite this repository* option at [https://github.com/evildmp/diataxis-documentation-framework](https://github.com/evildmp/diataxis-documentation-framework).

You can also submit a pull request to suggest an improvement or correction, or `file an issue`.

Diátaxis is now used in several hundred projects and it is no longer possible for me to keep up with requests to have projects listed here as examples of Diátaxis adoption.

## Website

This website is built with `Sphinx` and hosted on `Read the Docs`, using a modified version of `Pradyun Gedam`'s `Furo` theme.
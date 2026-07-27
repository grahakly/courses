# SYSTEM DESIGN IN 100 DAYS
## The World's Best System Design Course
### Written in Simple Language - Like Teaching a 14-Year-Old

---

**Author:** AI Course Designer
**Level:** Beginner to Expert
**Style:** Simple, Fun, with Real Examples & Memory Tricks

---

## TABLE OF CONTENTS

- **PHASE 1: Foundation (Days 1-20)** - Building Blocks
- **PHASE 2: Core Concepts (Days 21-40)** - The Main Ideas
- **PHASE 3: Building Blocks (Days 41-60)** - Components & Patterns
- **PHASE 4: Real System Designs (Days 61-85)** - Design Famous Systems
- **PHASE 5: Advanced & Interview Prep (Days 86-100)** - Master Level

---

## HOW TO USE THIS BOOK

1. **Read ONE day per day** - Don't rush!
2. **Draw diagrams** - Use pen and paper
3. **Explain to a friend** - If you can teach it, you know it
4. **Use the memory tricks** - They help you remember forever
5. **Do the mini-project** at end of each week

---


---

# PHASE 1: FOUNDATION (Days 1-20)
## Building Your System Design Superpowers

---

## DAY 1: What is System Design?

### The Big Idea
System Design is like being an **architect for software**. Just like an architect designs a building (where the doors go, how many floors, where the elevator is), a system designer decides how software is built.

### Real Life Example
Think about **Instagram**:
- Where do all the photos go? (Storage)
- How do millions of people see photos at the same time? (Servers)
- How does your feed load so fast? (Caching)
- What happens if one computer breaks? (Reliability)

**THAT is system design!**

### Memory Trick
**S.Y.S.T.E.M = Serve Your Software To Everyone Magnificently**

### Key Terms Today
| Term | Simple Meaning |
|------|---------------|
| Server | A powerful computer that serves data to users |
| Client | Your phone/laptop that asks for data |
| Database | A giant organized notebook that stores information |
| Network | The road between your phone and the server |

### Draw This
```
[Your Phone] ---internet---> [Server] ----> [Database]
   (Client)                  (Brain)        (Memory)
```

### Today's Quiz
1. What does a server do?
2. Name 3 things you'd need to design for Instagram.
3. What's the difference between a client and a server?

---


## DAY 2: Client-Server Architecture

### The Big Idea
Every app you use works like a **restaurant**:
- **You** (Client) = The customer
- **Waiter** (Internet) = Carries your order
- **Kitchen** (Server) = Makes your food
- **Pantry** (Database) = Stores ingredients

### How It Works
1. You open YouTube on your phone (Client sends request)
2. Request travels through the internet (Network)
3. YouTube's server receives it (Server processes)
4. Server gets the video from storage (Database query)
5. Video is sent back to your phone (Response)

### Memory Trick
**Think of ordering pizza online:**
- You = Client
- Pizza website = Server
- Order goes through internet = Network
- Pizza recipes stored = Database

### Types of Architecture
```
1. ONE SERVER (Simple)
   [Client] --> [Single Server + Database]
   Good for: Small apps, personal projects

2. SEPARATE SERVER & DATABASE (Better)
   [Client] --> [Server] --> [Database]
   Good for: Medium apps

3. MULTIPLE SERVERS (Best for big apps)
   [Client] --> [Load Balancer] --> [Server 1]
                                --> [Server 2] --> [Database]
                                --> [Server 3]
   Good for: Apps with millions of users
```

### Real Example: WhatsApp Message
1. You type "Hi" and press send (Client)
2. Message goes to WhatsApp server (Server receives)
3. Server checks: Is your friend online? (Processing)
4. If yes: Send directly. If no: Store in database (Decision)
5. Friend's phone gets the message (Delivery)

### Today's Quiz
1. In the restaurant analogy, what is the "waiter"?
2. Why would you need multiple servers?
3. Draw the journey of a WhatsApp message.

---


## DAY 3: Networks & Protocols (How Computers Talk)

### The Big Idea
Computers talk to each other using **rules** called protocols. It's like how we have rules for talking on the phone:
- You say "Hello" first
- You wait for the other person to respond
- You say "Bye" before hanging up

### The Main Protocols

**HTTP/HTTPS (HyperText Transfer Protocol)**
- Used by: Websites, Apps
- Like: Sending a letter and getting a reply
- Example: When you open google.com

**TCP (Transmission Control Protocol)**
- Used by: When you need ALL data to arrive
- Like: Sending a registered letter (you get confirmation)
- Example: Loading a webpage (every piece must arrive)

**UDP (User Datagram Protocol)**
- Used by: When speed matters more than perfection
- Like: Shouting in a crowd (some people might miss it)
- Example: Video calls, online gaming

### Memory Trick
- **TCP** = **T**akes **C**areful **P**ath (reliable, slow)
- **UDP** = **U**ltra **D**elivery **P**ower (fast, might lose some)

### IP Address
Every device on the internet has an address, like a home address.
- Example: `192.168.1.1`
- It's how computers find each other

### Port Numbers
Think of an IP address as an apartment building, and port as the apartment number.
- Port 80: HTTP (websites)
- Port 443: HTTPS (secure websites)
- Port 3306: MySQL database

```
Full address: 192.168.1.1:443
              [Building]  :[Apartment]
```

### DNS (Domain Name System)
Humans remember names, not numbers!
- You type: `www.google.com`
- DNS converts to: `142.250.80.46`
- Like a phone book for the internet!

### Today's Quiz
1. What's the difference between TCP and UDP?
2. What does DNS do?
3. Why does YouTube use UDP for video streaming?

---


## DAY 4: APIs - How Apps Talk to Each Other

### The Big Idea
An API (Application Programming Interface) is like a **menu at a restaurant**:
- The menu shows you what you CAN order
- You don't need to know HOW the kitchen makes it
- You just ask for what you want, and you get it!

### Real Example
When a weather app shows you temperature:
1. App asks Weather API: "What's the temperature in New York?"
2. API replies: "72 degrees, sunny"
3. App shows it to you beautifully

The app doesn't have a thermometer - it ASKS another service!

### Types of APIs

**REST API (Most Common)**
- Uses HTTP methods like a library system:
  - **GET** = Read a book (get data)
  - **POST** = Add a new book (create data)
  - **PUT** = Replace a book (update data)
  - **DELETE** = Remove a book (delete data)

```
GET /users/123        --> Give me info about user 123
POST /users           --> Create a new user
PUT /users/123        --> Update user 123's info
DELETE /users/123     --> Delete user 123
```

**GraphQL**
- Like ordering custom pizza: "I want only cheese and mushrooms"
- You ask for EXACTLY what you need, nothing more
- Facebook created it!

**gRPC**
- Super fast, like a bullet train
- Used when servers talk to each other
- Google created it!

### Memory Trick
**REST = Restaurant Style** - You pick from the menu
**GraphQL = Grocery Style** - You pick exact ingredients
**gRPC = Speed Style** - Fastest communication

### JSON - The Language of APIs
```json
{
  "name": "John",
  "age": 14,
  "hobbies": ["gaming", "coding", "reading"]
}
```
JSON is how data is packaged and sent. Like putting a letter in an envelope with a specific format.

### Today's Quiz
1. What HTTP method would you use to create a new post?
2. Why is GraphQL useful for mobile apps?
3. Write a JSON object for your favorite movie.

---


## DAY 5: Databases - Where Data Lives

### The Big Idea
A database is like a **super organized filing cabinet** that can find any file in milliseconds, even if there are billions of files!

### Two Main Types

**1. SQL Databases (Relational) - Like Excel Spreadsheets**
- Data stored in tables with rows and columns
- Everything is organized and connected
- Examples: MySQL, PostgreSQL, Oracle

```
USERS TABLE:
| id  | name    | email           | age |
|-----|---------|-----------------|-----|
| 1   | Alice   | alice@mail.com  | 25  |
| 2   | Bob     | bob@mail.com    | 30  |

POSTS TABLE:
| id  | user_id | content         | likes |
|-----|---------|-----------------|-------|
| 1   | 1       | "Hello World!"  | 50    |
| 2   | 2       | "Love coding"   | 120   |
```

**2. NoSQL Databases (Non-Relational) - Like a Storage Room**
- Data stored in flexible formats
- No strict rules about structure
- Examples: MongoDB, Cassandra, Redis

```json
{
  "id": 1,
  "name": "Alice",
  "posts": [
    {"content": "Hello World!", "likes": 50},
    {"content": "System Design is fun!", "likes": 200}
  ],
  "friends": ["Bob", "Charlie"]
}
```

### When to Use What?

| Use SQL When... | Use NoSQL When... |
|----------------|-------------------|
| Data has clear structure | Data changes shape often |
| You need complex queries | You need super fast reads |
| Banking, e-commerce | Social media, gaming |
| Relationships matter | Scale is massive |

### Memory Trick
- **SQL** = **S**tructured **Q**uery **L**anguage = Everything in neat boxes
- **NoSQL** = **N**ot **O**nly **SQL** = Flexible, like a backpack (throw anything in)

### ACID Properties (SQL's Superpowers)
- **A**tomicity: All or nothing (like a bank transfer - both accounts change or neither)
- **C**onsistency: Rules are always followed
- **I**solation: Transactions don't mess with each other
- **D**urability: Once saved, it stays saved forever

### Today's Quiz
1. Would you use SQL or NoSQL for a banking app? Why?
2. What does ACID stand for?
3. Give an example where NoSQL is better than SQL.

---


## DAY 6: Scaling - Handling More Users

### The Big Idea
Imagine your lemonade stand gets super popular. Yesterday 10 people came. Today 10,000 people want lemonade! What do you do?

**Scaling** = Making your system handle more users without breaking.

### Two Ways to Scale

**1. Vertical Scaling (Scale UP) - Get a BIGGER Machine**
- Like replacing your bicycle with a motorcycle
- Buy a more powerful server (more RAM, CPU, storage)
- Simple but has limits (you can't make one machine infinitely powerful)

```
Before: [Small Server - 4GB RAM]
After:  [HUGE Server - 256GB RAM]
```

**2. Horizontal Scaling (Scale OUT) - Get MORE Machines**
- Like hiring more lemonade sellers
- Add more servers that share the work
- Can scale almost infinitely!

```
Before: [1 Server handling everything]
After:  [Server 1] [Server 2] [Server 3] [Server 4]
        All sharing the work!
```

### Memory Trick
- **Vertical** = Think **V**ery big (one giant machine going UP)
- **Horizontal** = Think **H**erd (many machines standing side by side)

### Real Example: Netflix
- Netflix has 200+ million users
- They can't use one super computer
- They use THOUSANDS of servers (horizontal scaling)
- Servers are spread across the world

### The Problem with Horizontal Scaling
If you have many servers, how does a user know which one to talk to?
Answer: **Load Balancer** (We'll learn this tomorrow!)

### Comparison Table
| Feature | Vertical Scaling | Horizontal Scaling |
|---------|-----------------|-------------------|
| Cost | Expensive (big machines cost a lot) | Cheaper (many small machines) |
| Limit | Has a ceiling | Almost unlimited |
| Complexity | Simple | Complex (need coordination) |
| Downtime | Need to shut down to upgrade | Can add servers without stopping |
| Risk | Single point of failure | If one dies, others continue |

### Today's Quiz
1. Your app just got featured on TV and traffic jumped 100x. Which scaling do you choose? Why?
2. Why can't we just keep doing vertical scaling forever?
3. Name one company that uses horizontal scaling.

---


## DAY 7: Load Balancers - The Traffic Police

### The Big Idea
A Load Balancer is like a **traffic police officer** at a busy intersection. It directs cars (requests) to different roads (servers) so no single road gets too crowded.

### Why We Need It
Without a load balancer:
```
10,000 requests --> [Server 1] --> CRASH! Too much!
```

With a load balancer:
```
10,000 requests --> [Load Balancer] --> [Server 1] 3,333 requests
                                    --> [Server 2] 3,333 requests
                                    --> [Server 3] 3,334 requests
                                    Happy servers!
```

### Load Balancing Algorithms

**1. Round Robin** (Take turns)
- Request 1 -> Server A
- Request 2 -> Server B
- Request 3 -> Server C
- Request 4 -> Server A (back to start)
- Like dealing cards in a card game!

**2. Least Connections** (Who's least busy?)
- Send to the server handling fewest requests right now
- Like choosing the shortest line at a grocery store

**3. IP Hash** (Same person, same server)
- Your IP address decides which server you go to
- Like having your own assigned desk at school

**4. Weighted Round Robin** (Stronger servers get more)
- Powerful server gets 5 requests, weak one gets 2
- Like giving more homework to the smartest student

### Memory Trick
**L.O.A.D = Levels Out All Demands**

### Real World Load Balancers
- **Nginx** - Very popular, free
- **AWS ELB** - Amazon's cloud load balancer
- **HAProxy** - High performance

### Types of Load Balancers
```
Layer 4 (Transport): Looks at IP address and port
  - Faster, simpler
  - Like sorting mail by zip code

Layer 7 (Application): Looks at actual content
  - Smarter, can route based on URL
  - Like reading the letter to decide where it goes
```

### Today's Quiz
1. What load balancing algorithm is best for a gaming server?
2. What happens if the load balancer itself crashes?
3. Draw a system with 2 load balancers and 4 servers.

---

## DAY 8: Caching - The Speed Superpower

### The Big Idea
Caching is like keeping your **favorite snacks on your desk** instead of walking to the kitchen every time. The data you use most often is stored closer to you!

### Why Caching Matters
- Database query: 100 milliseconds (slow)
- Cache lookup: 1 millisecond (100x faster!)

### Real Life Caching
1. **Your brain** caches multiplication tables (you don't calculate 7x8 each time)
2. **Your browser** caches website images (doesn't re-download Google's logo)
3. **YouTube** caches popular videos near you

### Where to Cache?

```
[User] --> [Browser Cache] --> [CDN Cache] --> [App Server Cache] --> [Database Cache] --> [Database]
 Fastest                                                                                    Slowest
```

### Cache Strategies

**1. Cache-Aside (Lazy Loading)**
```
1. App asks cache: "Do you have this data?"
2. Cache: "No" (Cache Miss)
3. App asks database, gets data
4. App stores data in cache for next time
5. Next request: Cache says "YES!" (Cache Hit)
```

**2. Write-Through**
```
1. App writes data to cache AND database at same time
2. Always in sync, but slower writes
```

**3. Write-Behind (Write-Back)**
```
1. App writes to cache only (super fast!)
2. Cache writes to database later (in background)
3. Risk: If cache dies before writing, data is lost!
```

### Memory Trick
**CACHE = Commonly Accessed Content Held for Efficiency**

### Popular Cache Tools
- **Redis** - Most popular, stores data in memory
- **Memcached** - Simple and fast
- **CDN** (Content Delivery Network) - Caches content worldwide

### Cache Problems

**1. Cache Invalidation** (When to update the cache?)
- "There are only two hard things in computer science: cache invalidation and naming things" - Phil Karlton

**2. Cache Stampede** (Everyone asks at once)
- Cache expires, 1000 users all hit database simultaneously!

### Today's Quiz
1. Why is cache faster than a database?
2. What's a cache miss?
3. When would write-behind cache be dangerous?

---


## DAY 9: CDN - Content Delivery Network

### The Big Idea
A CDN is like having **copies of a popular book in every library in the world** instead of just one library. When someone wants the book, they go to the nearest library!

### The Problem CDN Solves
Without CDN:
- A user in Japan loads a website hosted in USA
- Data travels 10,000 km = SLOW (300ms delay)

With CDN:
- Website content is copied to a server in Japan
- User gets data from nearby server = FAST (20ms delay)

### How CDN Works
```
                    [Origin Server - USA]
                    /        |        \
   [CDN Edge-Tokyo]  [CDN Edge-London]  [CDN Edge-Sydney]
        |                    |                    |
   [Users in Asia]    [Users in Europe]    [Users in Australia]
```

### What CDN Stores
- Images and videos
- CSS and JavaScript files
- Static HTML pages
- Downloads (apps, PDFs)
- Streaming content

### Memory Trick
**CDN = Copies Distributed Nearby**

### Real Examples
- **Netflix** uses CDN to stream movies (their CDN is called Open Connect)
- **Instagram** stores your photos on CDN
- **Gaming** - Game updates download from nearest CDN

### Popular CDN Providers
- CloudFlare (also provides security)
- AWS CloudFront
- Akamai (one of the oldest)
- Google Cloud CDN

### Push vs Pull CDN

**Push CDN:**
- YOU upload content to CDN manually
- Good for: Content that doesn't change often
- Like: Putting books on library shelves yourself

**Pull CDN:**
- CDN automatically grabs content when first requested
- Good for: Dynamic content
- Like: Library orders a book when someone first asks for it

### Today's Quiz
1. Why is a CDN faster than a single server?
2. Would you use CDN for a banking transaction? Why or why not?
3. What's the difference between Push and Pull CDN?

---

## DAY 10: Database Indexing - Finding Things Fast

### The Big Idea
An index in a database is like the **index at the back of a textbook**. Without it, you'd have to read every single page to find what you want!

### The Problem
Imagine a database with 1 BILLION users:
- Without index: Check all 1 billion rows = 10 minutes!
- With index: Jump directly to the right row = 0.001 seconds!

### How Indexing Works
```
Without Index (Full Table Scan):
Page 1 -> Page 2 -> Page 3 -> ... -> Page 1,000,000 -> FOUND IT!

With Index (B-Tree):
Start -> Is it > M? Yes -> Is it > S? No -> Check P-S section -> FOUND "Smith"!
(Only 3 steps instead of 1 million!)
```

### Real Life Analogy
Finding "elephant" in a dictionary:
- **Without index**: Read every word from A to E... (hours!)
- **With index**: Go to "E" section, then "El"... (seconds!)

### Types of Indexes

**1. Primary Index** (Main ID)
- Like a student roll number
- Every table should have one
- Usually the ID column

**2. Secondary Index** (Extra shortcuts)
- Like an index by subject in a library
- Example: Index on "email" column for fast login

**3. Composite Index** (Multiple columns)
- Like finding a book by BOTH author AND title
- Example: Index on (city, age) for queries like "all 25-year-olds in NYC"

### Memory Trick
**INDEX = Instant Navigational Data for EXtreme speed**

### The Trade-off
- Good: Reading is SUPER fast
- Bad: Writing is slightly slower (need to update the index too)
- Bad: Takes extra storage space

### When to Create an Index
- Columns you search by often (WHERE clause)
- Columns you sort by (ORDER BY)
- Columns you join on

### When NOT to Create an Index
- Small tables (full scan is fine)
- Columns that change constantly
- Columns with few unique values (like gender: M/F)

### Today's Quiz
1. Why does an index make reads faster but writes slower?
2. Would you index a column with only 2 possible values?
3. What data structure do most indexes use?

---


## DAY 11: Database Replication - Copies for Safety

### The Big Idea
Database replication is like having **backup copies of your homework** - if you lose one, you still have others! It also lets multiple people read different copies at the same time.

### Why Replicate?
1. **Safety**: If one database dies, others have the data
2. **Speed**: Users read from the nearest copy
3. **Load**: Spread reading across multiple copies

### Master-Slave (Leader-Follower) Pattern
```
[Users Write] --> [Master DB] -- copies to --> [Slave 1] <-- [Users Read]
                                           --> [Slave 2] <-- [Users Read]
                                           --> [Slave 3] <-- [Users Read]
```
- **Master**: Handles ALL writes
- **Slaves**: Handle reads (copies of master)
- One master, many slaves

### Master-Master Pattern
```
[Users] --> [Master 1] <-- syncs --> [Master 2] <-- [Users]
```
- Both can handle reads AND writes
- More complex (what if both write at the same time?)

### Memory Trick
**REPLICA = Redundant Extra Protection Locally In Case of Accidents**

### Replication Lag
- The time it takes for slave to get master's latest data
- Usually milliseconds, but can be seconds
- Problem: User writes to master, reads from slave, doesn't see their own update!

### Solution: Read-Your-Own-Writes
- After a user writes, read from MASTER for that user
- Everyone else reads from slaves
- Best of both worlds!

### Today's Quiz
1. Why can't all databases be masters?
2. What is replication lag?
3. If the master dies, what happens?

---

## DAY 12: Database Sharding - Splitting Data

### The Big Idea
Sharding is like splitting a **giant phonebook into smaller books** - one for A-F, one for G-L, etc. Each piece is easier to manage and search!

### Why Shard?
- Your database has 10 BILLION rows
- One machine can't hold it all
- Solution: Split data across multiple machines!

### How Sharding Works
```
All Users (10 billion)
        |
   [Shard Key: First letter of username]
        |
[Shard 1: A-F]  [Shard 2: G-L]  [Shard 3: M-R]  [Shard 4: S-Z]
 2.5 billion      2.5 billion      2.5 billion      2.5 billion
```

### Sharding Strategies

**1. Range-Based Sharding**
- Split by ranges: Users 1-1M on Shard 1, 1M-2M on Shard 2
- Problem: Uneven distribution (what if most users have IDs 1-1M?)

**2. Hash-Based Sharding**
- Apply math formula to decide which shard
- hash(user_id) % number_of_shards = shard_number
- More even distribution!

**3. Geographic Sharding**
- US users on US shard, European users on EU shard
- Faster for users (data is nearby)

### Memory Trick
**SHARD = Split Horizontally Across Replicated Databases**

### Problems with Sharding
1. **Joins are hard**: Data on different machines can't easily be combined
2. **Rebalancing**: Adding a new shard means moving data around
3. **Hotspots**: One shard might get way more traffic

### Real Example
- **Instagram** shards by user_id
- **Discord** shards by server (guild) ID
- **Uber** shards by geographic location

### Today's Quiz
1. What's the difference between sharding and replication?
2. Why is hash-based sharding more even than range-based?
3. A social media app has 500 million users. Design a sharding strategy.

---


## DAY 13: Consistent Hashing - Smart Data Distribution

### The Big Idea
Consistent hashing is like arranging people in a **circle** instead of a line. When someone leaves or joins, only their neighbors are affected, not everyone!

### The Problem It Solves
Regular hashing: `server = hash(key) % N`
- If you add/remove a server (N changes), EVERYTHING moves!
- Like rearranging ALL lockers when one new locker is added.

Consistent hashing:
- Only ~1/N of the data moves when a server changes
- Like adding a new seat at a round table - only neighbors shift

### How It Works
```
Imagine a clock (circle from 0 to 360 degrees):

        0/360
         |
   Server A (at 90)
         |
   330 --+-- 90
         |
   Server C (at 210)    Server B (at 150)
         |
        180

Data "photo_123" hashes to position 120 -> goes to Server B (next clockwise)
Data "video_456" hashes to position 200 -> goes to Server C (next clockwise)
```

### When a Server Joins/Leaves
- **Server B dies**: Only B's data moves to next server (C)
- Other servers are NOT affected!
- Compare: Regular hashing would reshuffle everything

### Memory Trick
**Think of it as a CLOCK - data goes to the next server clockwise. Adding/removing a server only affects the slice next to it.**

### Virtual Nodes (Making it Even)
Problem: Servers might be unevenly spaced on the circle
Solution: Each real server gets multiple positions (virtual nodes)

```
Server A gets positions: 30, 120, 250
Server B gets positions: 70, 180, 330
Now the load is much more even!
```

### Where It's Used
- **Amazon DynamoDB** - Distributed database
- **Apache Cassandra** - NoSQL database
- **Discord** - Distributing chat servers
- **Memcached** - Distributed caching

### Today's Quiz
1. Why is consistent hashing better than regular hashing for distributed systems?
2. What are virtual nodes and why do we need them?
3. If we have 5 servers and add a 6th, how much data moves?

---

## DAY 14: CAP Theorem - The Impossible Triangle

### The Big Idea
The CAP Theorem says that in a distributed system, you can only have **2 out of 3** things. It's like saying you can only pick 2 toppings on your pizza, never all 3!

### The Three Properties

**C - Consistency**: Every read gets the LATEST data
- Like: Everyone sees the same scoreboard at the same time

**A - Availability**: System ALWAYS responds (never says "come back later")
- Like: The store is ALWAYS open, never closed

**P - Partition Tolerance**: System works even if network breaks between servers
- Like: The school still functions even if the intercom breaks

### The Rule
In real distributed systems, network issues WILL happen (P is required).
So you really choose between:
- **CP** (Consistency + Partition Tolerance): Always correct data, might be unavailable sometimes
- **AP** (Availability + Partition Tolerance): Always available, might show slightly old data

### Memory Trick
**CAP = Can't Always Pick (all three)**

### Real World Examples

| System | Choice | Why |
|--------|--------|-----|
| Banks | CP | Money MUST be accurate (you'd rather wait than get wrong balance) |
| Social Media | AP | Better to show an old post than show nothing |
| Google Search | AP | Better to show some results than "Google is down" |
| Stock Trading | CP | Prices MUST be accurate |
| Shopping Cart | AP | Better to let users add items than say "try later" |

### Visual
```
        Consistency
           /\
          /  \
    CP   /    \  CA (not possible in real distributed systems)
        /      \
       /________\
Partition        Availability
Tolerance
       \________/
           AP
```

### Today's Quiz
1. Why is Partition Tolerance usually required?
2. Would you choose CP or AP for a chat application?
3. Can a single-server system have all three? Why?

---


## DAY 15: Message Queues - The Post Office of Systems

### The Big Idea
A message queue is like a **post office mailbox**. The sender drops a letter and walks away. The receiver picks it up whenever they're ready. They don't need to be available at the same time!

### Why Message Queues?
Without queue (synchronous):
```
[User] --> [Server A] --> waits --> [Server B processes] --> response
User waits the ENTIRE time!
```

With queue (asynchronous):
```
[User] --> [Server A] --> drops message in queue --> "Done!" (immediate response)
                          [Queue] --> [Server B picks up and processes later]
```

### Real Examples

**1. Email Sending**
- You sign up for a website
- Server says "Welcome!" immediately
- Welcome email is queued and sent in background (you don't wait for it)

**2. Video Processing (YouTube)**
- You upload a video
- YouTube says "Processing..." immediately
- Video encoding happens in background via queue

**3. Food Delivery**
- Order placed -> confirmation shown immediately
- Restaurant notified via queue
- Driver assigned via queue

### Key Concepts

**Producer**: Sends messages (like you sending a letter)
**Consumer**: Receives and processes messages (like the recipient)
**Queue**: Stores messages in between (like the mailbox)

```
[Producer] --> [Queue: msg1, msg2, msg3] --> [Consumer]
```

### Popular Message Queues
- **RabbitMQ** - Easy to use, reliable
- **Apache Kafka** - Super high-throughput, used by LinkedIn/Netflix
- **Amazon SQS** - Cloud-based, managed by AWS
- **Redis** - Can also work as a simple queue

### Memory Trick
**QUEUE = Quickly Ushers Updates for Eventual Execution**

### Benefits
1. **Decoupling**: Services don't depend on each other directly
2. **Resilience**: If consumer dies, messages wait in queue
3. **Scalability**: Add more consumers to process faster
4. **Smoothing**: Handle traffic spikes gracefully

### Today's Quiz
1. Why would YouTube use a message queue for video uploads?
2. What happens if the consumer is down?
3. Name 3 scenarios where async processing is better than sync.

---

## DAY 16: Microservices vs Monolith

### The Big Idea
Imagine building with LEGO blocks vs carving from one big rock:
- **Monolith** = One big rock (everything together)
- **Microservices** = LEGO blocks (small pieces that fit together)

### Monolith Architecture
```
[ONE BIG APPLICATION]
|-- User Management
|-- Payment Processing
|-- Email Service
|-- Search
|-- Notifications
|-- Analytics
ALL in ONE codebase, ONE deployment
```

**Pros:**
- Simple to develop initially
- Easy to test (everything is together)
- Simple deployment (one thing to deploy)

**Cons:**
- Gets messy as it grows (spaghetti code)
- One bug can crash EVERYTHING
- Can't scale parts independently
- Team conflicts (everyone works on same code)

### Microservices Architecture
```
[User Service]     [Payment Service]    [Email Service]
[Search Service]   [Notification Service]  [Analytics Service]
Each is independent! Each has its own database!
```

**Pros:**
- Scale each service independently
- Different teams own different services
- One crash doesn't affect others
- Use best technology for each service

**Cons:**
- Complex communication between services
- Harder to debug across services
- Need infrastructure for service discovery
- Data consistency is harder

### Memory Trick
- **MONO** = ONE (like monolingual = one language)
- **MICRO** = TINY (like microscope = seeing tiny things)

### When to Use What?

| Startup (< 5 engineers) | Big Company (100+ engineers) |
|--------------------------|------------------------------|
| Use Monolith | Use Microservices |
| Move fast, iterate | Scale independently |
| Simple deployment | Team autonomy |

### Real Examples
- **Netflix**: Started as monolith, migrated to 700+ microservices
- **Amazon**: Each team owns their own service
- **Uber**: Separate services for rides, payments, maps, matching

### Today's Quiz
1. Why did Netflix move from monolith to microservices?
2. For a brand new startup with 3 engineers, which would you recommend?
3. What's the biggest challenge with microservices?

---


## DAY 17: Rate Limiting - Preventing Abuse

### The Big Idea
Rate limiting is like a **bouncer at a club** - only letting a certain number of people in per hour. It prevents any single user from overwhelming your system!

### Why Rate Limiting?
- Prevent DDoS attacks (hackers flooding your system)
- Ensure fair usage (one user can't hog everything)
- Control costs (API calls cost money)
- Protect backend services from overload

### Common Algorithms

**1. Token Bucket**
```
Bucket holds 10 tokens. Each request takes 1 token.
Tokens refill at rate of 2 per second.
- Request 1-10: Allowed (10 tokens used)
- Request 11: DENIED (bucket empty)
- Wait 1 second: 2 tokens refilled
- Request 12-13: Allowed
```
Like: A candy machine that drops 2 candies per minute

**2. Sliding Window**
```
Window = last 60 seconds
Rule = Max 100 requests per minute

Time 0:00 - 0:59: You made 100 requests (at limit!)
Time 0:30 - 1:29: Count only requests in THIS window
```
Like: Counting cars on a highway in the last hour

**3. Fixed Window**
```
Each minute resets the counter
Minute 1: 0/100 used... 50/100... 100/100 -> BLOCKED
Minute 2: Counter resets! 0/100 again
```

### Memory Trick
**RATE LIMIT = Restricting Access To Ensure Lasting Integrity & Managed Traffic**

### Where to Apply Rate Limiting
1. **API Gateway** - Before requests reach your servers
2. **Per User** - Each user gets their own limit
3. **Per IP** - Prevent one computer from flooding
4. **Per Endpoint** - Login page has stricter limits

### Real Examples
- **Twitter/X**: 300 tweets per 3 hours
- **GitHub API**: 5000 requests per hour
- **Google Maps**: 25,000 map loads per day (free tier)

### HTTP Response When Rate Limited
```
HTTP 429 - Too Many Requests
Headers:
  X-RateLimit-Limit: 100
  X-RateLimit-Remaining: 0
  Retry-After: 30 seconds
```

### Today's Quiz
1. What HTTP status code means "rate limited"?
2. Why would you rate limit a login endpoint more strictly?
3. Design a rate limiter for an API that allows 1000 requests/minute.

---

## DAY 18: Proxies - The Middlemen

### The Big Idea
A proxy is like a **personal assistant** who talks to people on your behalf. You tell the assistant what you need, and they go get it for you.

### Forward Proxy (Client-side)
Sits between users and the internet. Protects the CLIENT.
```
[User] --> [Forward Proxy] --> [Internet/Servers]
```
**Use cases:**
- Hide your IP address (privacy)
- Access blocked websites (school/work)
- Cache frequently accessed content
- Filter content (parental controls)

### Reverse Proxy (Server-side)
Sits between internet and servers. Protects the SERVER.
```
[Internet/Users] --> [Reverse Proxy] --> [Server 1]
                                     --> [Server 2]
                                     --> [Server 3]
```
**Use cases:**
- Load balancing (distribute traffic)
- SSL termination (handle encryption)
- Caching (serve cached content fast)
- Security (hide server details)

### Memory Trick
- **Forward** proxy = **F**or the client (Forward = Front of client)
- **Reverse** proxy = **R**ear guard for servers (Reverse = Behind, protecting servers)

### Real Examples
- **Nginx** - Most popular reverse proxy
- **VPN** - Type of forward proxy
- **CloudFlare** - Reverse proxy + CDN + security
- **Corporate networks** - Forward proxy to filter employee internet

### Today's Quiz
1. What's the difference between forward and reverse proxy?
2. When you use a VPN, what type of proxy is it?
3. Why does Netflix use a reverse proxy?

---


## DAY 19: Latency vs Throughput

### The Big Idea
- **Latency** = How FAST one thing gets done (speed of one car)
- **Throughput** = How MUCH gets done in a period (cars per hour on highway)

### Analogy: Water Pipes
- **Latency** = How quickly the first drop reaches the other end
- **Throughput** = How much water flows per second (depends on pipe width)

A thin pipe can have low latency (short pipe) but low throughput.
A wide pipe can have high throughput but maybe high latency (long pipe).

### Numbers Every Engineer Should Know
| Operation | Time |
|-----------|------|
| L1 cache reference | 0.5 nanoseconds |
| L2 cache reference | 7 nanoseconds |
| RAM reference | 100 nanoseconds |
| SSD read | 150 microseconds |
| Hard disk read | 10 milliseconds |
| Send packet US to Europe | 150 milliseconds |
| Read 1 MB from SSD | 1 millisecond |
| Read 1 MB from disk | 20 milliseconds |
| Read 1 MB from network | 10 milliseconds |

### Memory Trick
**Latency = Late (how late is the response?)**
**Throughput = Through (how much goes through?)**

### How to Improve Latency
1. Cache data closer to user
2. Use CDN
3. Reduce number of network hops
4. Use faster storage (SSD instead of HDD)
5. Compress data before sending

### How to Improve Throughput
1. Add more servers (horizontal scaling)
2. Use wider network bandwidth
3. Process things in parallel (batching)
4. Use message queues for async processing
5. Optimize database queries

### Real Example
**Google Search:**
- Latency goal: < 200ms per search
- Throughput: 8.5 billion searches per day = ~100,000 per second

### Today's Quiz
1. Can you have low latency but low throughput?
2. What's more important for a video game: latency or throughput?
3. What's more important for file downloads: latency or throughput?

---

## DAY 20: System Design Framework (How to Approach ANY Problem)

### The Big Idea
When someone asks you to "Design Twitter" or "Design Uber", don't panic! Follow this **4-step framework** every single time.

### The STAR Framework for System Design

**S - Scope (3-5 minutes)**
- What features do we need?
- How many users?
- What are the constraints?
- Ask clarifying questions!

**T - Think High Level (5-10 minutes)**
- Draw the big picture
- Identify main components
- Show data flow

**A - Architect in Detail (15-20 minutes)**
- Database schema
- API design
- Deep dive into key components
- Discuss trade-offs

**R - Review & Resolve (5 minutes)**
- Identify bottlenecks
- Discuss scalability
- Handle edge cases
- Mention monitoring/alerting

### Memory Trick
**STAR = Scope, Think, Architect, Review**
(Like getting a gold STAR for your design!)

### Example: "Design a URL Shortener"

**S - Scope:**
- How many URLs per day? 100 million
- How long to keep them? 5 years
- Custom short URLs? Yes
- Analytics needed? Click count

**T - Think High Level:**
```
[User] --> [Load Balancer] --> [App Server] --> [Database]
                                    |
                                 [Cache]
```

**A - Architect:**
- Short URL generation: Base62 encoding
- Database: NoSQL (simple key-value)
- Cache: Redis for hot URLs
- Read-heavy system (100:1 read/write ratio)

**R - Review:**
- Bottleneck: Database for popular URLs -> Cache solves this
- Scale: Shard by first character of short URL
- Edge case: What if two people want same custom URL?

### Week 1-3 Summary Checklist
- [ ] Client-Server architecture
- [ ] Networks & Protocols
- [ ] APIs (REST, GraphQL, gRPC)
- [ ] Databases (SQL vs NoSQL)
- [ ] Scaling (Vertical vs Horizontal)
- [ ] Load Balancers
- [ ] Caching
- [ ] CDN
- [ ] Indexing
- [ ] Replication & Sharding
- [ ] Consistent Hashing
- [ ] CAP Theorem
- [ ] Message Queues
- [ ] Microservices
- [ ] Rate Limiting
- [ ] Proxies
- [ ] Latency vs Throughput
- [ ] System Design Framework

---

# MINI PROJECT: Design a Simple Chat Application
Design a basic chat app (like WhatsApp) with:
- 1-on-1 messaging
- Group chat (up to 100 people)
- Online/offline status
- Message delivery status (sent, delivered, read)

Draw the architecture and identify which concepts from Days 1-20 you'd use!

---


---

# PHASE 2: CORE CONCEPTS (Days 21-40)
## Deepening Your Knowledge

---

## DAY 21: Availability & Reliability

### The Big Idea
- **Availability** = Is the system UP right now? (Can I use it?)
- **Reliability** = Does the system work CORRECTLY over time? (Can I trust it?)

A system can be available but unreliable (website is up but shows wrong data).

### The Nines of Availability
| Availability | Downtime/Year | Called |
|-------------|---------------|--------|
| 99% | 3.65 days | Two nines |
| 99.9% | 8.76 hours | Three nines |
| 99.99% | 52.6 minutes | Four nines |
| 99.999% | 5.26 minutes | Five nines |
| 99.9999% | 31.5 seconds | Six nines |

### Memory Trick
**Each nine = 10x less downtime**
- Google targets: 99.99% (52 min downtime/year)
- AWS targets: 99.99% for most services
- A pacemaker: 99.9999% (life depends on it!)

### How to Achieve High Availability
1. **Redundancy**: Multiple copies of everything
2. **Failover**: Automatic switch to backup
3. **Health Checks**: Constantly monitor if things are working
4. **No Single Point of Failure (SPOF)**: If ONE thing breaking kills everything, that's bad!

### Single Point of Failure (SPOF)
```
BAD:  [Users] --> [ONE Server] --> [ONE Database]
      If server dies = EVERYTHING dies!

GOOD: [Users] --> [Load Balancer] --> [Server 1] --> [DB Primary]
                  [LB Backup]     --> [Server 2] --> [DB Replica]
                                  --> [Server 3] --> [DB Replica]
      Multiple failures needed to bring system down!
```

### Failover Types
- **Active-Passive**: One works, one waits (like a backup generator)
- **Active-Active**: Both work, share load (like two doors to a store)

### Today's Quiz
1. What's the downtime per year for 99.9% availability?
2. Find the SPOF in this design: Users -> Server -> Database
3. Which is better: Active-Active or Active-Passive? Why?

---

## DAY 22: Data Consistency Patterns

### The Big Idea
When you have multiple copies of data, how do you keep them in sync?
Like: If you update your profile photo, when do all your friends see the new one?

### Consistency Levels

**1. Strong Consistency**
- Everyone sees the same data at the same time
- Like: Bank balance (must be exact!)
- Slow but accurate
- Example: After transferring money, balance is immediately correct everywhere

**2. Eventual Consistency**
- Data will be the same EVENTUALLY (might take seconds)
- Like: Social media likes (it's okay if count is slightly off for a moment)
- Fast but temporarily inaccurate
- Example: You post a photo, friends see it a few seconds later

**3. Causal Consistency**
- Related events appear in correct order
- Like: In a chat, replies always appear after the original message
- Middle ground

### Memory Trick
- **Strong** = **S**ynchronized **I**nstantly
- **Eventual** = **E**ventually **E**veryone sees it
- **Causal** = **C**ause before effect

### Real World Choices
| System | Consistency | Why |
|--------|------------|-----|
| Banking | Strong | Money must be exact |
| Instagram Likes | Eventual | Who cares if it's 999 vs 1000 for 2 seconds? |
| Google Docs | Strong | Multiple editors must see same thing |
| DNS | Eventual | OK if new website takes hours to propagate |
| Stock prices | Strong | Traders need exact prices |

### Today's Quiz
1. Why is strong consistency slower?
2. Would a shopping cart use strong or eventual consistency?
3. Give an example where eventual consistency is dangerous.

---

## DAY 23: Hashing & Checksums

### The Big Idea
Hashing is like a **fingerprint for data**. You take any data (a file, password, message) and create a fixed-size unique identifier.

### Properties of a Good Hash
1. **Same input = Same output** (always)
2. **Different input = Different output** (usually)
3. **Can't reverse it** (can't get original from hash)
4. **Small change = Completely different hash**

### Example
```
hash("Hello") = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c..."
hash("hello") = "b6ef26b11e18305c6c4aa87e5bfe7e0a2818c5f3..."
hash("Hello!") = "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2..."
```
Notice: Tiny changes create completely different hashes!

### Use Cases

**1. Password Storage**
- NEVER store passwords as plain text!
- Store hash instead: hash("MyPassword123") = "a1b2c3d4..."
- To verify: hash the input and compare hashes

**2. Data Integrity**
- Download a file + its hash
- Hash the downloaded file
- Compare: If hashes match, file is not corrupted!

**3. Hash Tables** (for fast data lookup)
- hash("user_123") tells you which bucket/server to look in

**4. Deduplication**
- Hash all files. Same hash? It's a duplicate!

### Common Hash Algorithms
- **MD5** - Fast but not secure (don't use for passwords)
- **SHA-256** - Secure, used in Bitcoin
- **bcrypt** - Best for passwords (intentionally slow)

### Memory Trick
**HASH = Has A Specific Handle (unique identifier for anything)**

### Today's Quiz
1. Why should you NEVER store plain text passwords?
2. What happens if two different inputs produce the same hash? (hint: collision)
3. Why is bcrypt "intentionally slow"?

---


## DAY 24: WebSockets & Real-Time Communication

### The Big Idea
Normal HTTP is like sending letters - you send a request, get a response, connection closes.
WebSockets are like a **phone call** - once connected, both sides can talk anytime!

### HTTP vs WebSocket
```
HTTP (Half-duplex):
Client: "Any new messages?" --> Server: "No"
Client: "Any new messages?" --> Server: "No"
Client: "Any new messages?" --> Server: "Yes! Here it is"
(Client keeps asking... wasteful!)

WebSocket (Full-duplex):
Client: "Let's stay connected" --> Server: "OK, connection open!"
Server: "Hey! New message for you!" (anytime, without asking)
Client: "Thanks! Here's my reply" (anytime too)
```

### When to Use WebSockets
- Chat applications (WhatsApp, Slack)
- Live sports scores
- Stock ticker (real-time prices)
- Online gaming (multiplayer)
- Live collaborative editing (Google Docs)
- Notifications

### When NOT to Use WebSockets
- Simple CRUD apps (blog, e-commerce catalog)
- One-time data fetches
- File uploads

### Other Real-Time Options

**1. Polling (Checking repeatedly)**
```
Every 5 seconds: "Anything new?" "Anything new?" "Anything new?"
Simple but wasteful!
```

**2. Long Polling (Patient waiting)**
```
Client: "Tell me when something happens"
Server: [waits... waits... waits... 30 seconds]
Server: "Here's an update!"
Client: Immediately asks again
```

**3. Server-Sent Events (SSE)**
```
One-way: Server --> Client (only server pushes)
Good for: Notifications, news feeds
Can't send from client!
```

### Memory Trick
- **HTTP** = **H**ello, here's my question, goodbye
- **WebSocket** = **W**e're **S**taying connected

### Today's Quiz
1. Why would an online game use WebSockets instead of HTTP?
2. What's the disadvantage of polling?
3. When would you choose SSE over WebSockets?

---

## DAY 25: Authentication & Authorization

### The Big Idea
- **Authentication (AuthN)** = WHO are you? (Proving your identity)
- **Authorization (AuthZ)** = WHAT can you do? (Permissions)

Like entering a company building:
- Authentication = Showing your ID badge (proving who you are)
- Authorization = Your badge only opens certain doors (what you're allowed to access)

### Authentication Methods

**1. Password-Based**
- Username + Password
- Simple but can be stolen
- Always hash passwords!

**2. Token-Based (JWT)**
```
1. User logs in with username/password
2. Server creates a token (like a wristband at a concert)
3. User sends token with every request
4. Server verifies token (no need to check database each time!)
```

**3. OAuth 2.0 (Login with Google/Facebook)**
```
1. User clicks "Login with Google"
2. Google asks: "Allow this app to see your info?"
3. User says "Yes"
4. Google gives app a token
5. App uses token to get user's info from Google
```

**4. Multi-Factor Authentication (MFA)**
- Something you KNOW (password)
- Something you HAVE (phone with OTP)
- Something you ARE (fingerprint)

### JWT (JSON Web Token) - Deep Dive
```
Header.Payload.Signature
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjN9.abc123signature

Header: {"alg": "HS256"} (algorithm used)
Payload: {"user_id": 123, "role": "admin", "exp": 1234567890}
Signature: Proves the token hasn't been tampered with
```

### Memory Trick
- **AuthN** = "Are you **N**amed who you say?" (Identity)
- **AuthZ** = "Are you **Z**oned for this?" (Permission)

### Session vs Token

| Sessions | Tokens (JWT) |
|----------|-------------|
| Stored on server | Stored on client |
| Server remembers you | Server is stateless |
| Hard to scale | Easy to scale |
| Server uses memory | No server memory needed |

### Today's Quiz
1. What's the difference between authentication and authorization?
2. Why is JWT good for microservices?
3. What are the 3 factors in multi-factor authentication?

---


## DAY 26: Logging, Monitoring & Alerting

### The Big Idea
If your system is a car, then:
- **Logging** = The dashboard cam (records everything that happens)
- **Monitoring** = The dashboard gauges (speed, fuel, temperature)
- **Alerting** = The warning lights (tells you when something's wrong)

### Logging
What to log:
- Errors and exceptions
- User actions (login, purchase)
- Performance data (response times)
- Security events (failed logins)

Log Levels:
```
DEBUG:   Very detailed, for development only
INFO:    Normal operations ("User 123 logged in")
WARN:    Something unusual but not broken ("Disk 80% full")
ERROR:   Something failed ("Payment failed for user 123")
FATAL:   System is crashing ("Database connection lost")
```

### Monitoring
Key Metrics (The 4 Golden Signals):
1. **Latency** - How long requests take
2. **Traffic** - How many requests per second
3. **Errors** - How many requests fail
4. **Saturation** - How full is your system (CPU, memory, disk)

### Alerting Rules
```
IF response_time > 2 seconds for 5 minutes THEN alert
IF error_rate > 5% for 1 minute THEN page on-call engineer
IF disk_usage > 90% THEN warn
IF server is down for 30 seconds THEN critical alert
```

### Memory Trick
**LMA = Logs Monitor Alerts** (in that order)
- First: LOG everything
- Then: MONITOR the patterns
- Finally: ALERT when something's wrong

### Tools
- **Logging**: ELK Stack (Elasticsearch + Logstash + Kibana), Splunk
- **Monitoring**: Prometheus, Grafana, Datadog
- **Alerting**: PagerDuty, OpsGenie

### Today's Quiz
1. What are the 4 Golden Signals?
2. What log level would "Database connection slow" be?
3. Design an alerting rule for a payment system.

---

## DAY 27: Storage Systems - Blob, File, Block

### The Big Idea
Different types of data need different types of storage, just like you store clothes in a closet, food in a fridge, and books on a shelf!

### Types of Storage

**1. Block Storage (Like a hard disk)**
- Raw chunks of data
- Fastest, lowest level
- Used for: OS drives, databases
- Examples: AWS EBS, SAN

**2. File Storage (Like a file cabinet)**
- Organized in folders and files
- Has a path: /home/photos/vacation.jpg
- Used for: Shared drives, documents
- Examples: NFS, AWS EFS

**3. Object/Blob Storage (Like a warehouse)**
- Flat storage, each object has a unique key
- Unlimited scale
- Used for: Images, videos, backups, logs
- Examples: AWS S3, Google Cloud Storage

### Comparison
| Feature | Block | File | Object |
|---------|-------|------|--------|
| Speed | Fastest | Medium | Slowest |
| Scale | Limited | Medium | Unlimited |
| Cost | Expensive | Medium | Cheapest |
| Best for | Databases | Shared files | Media, backups |
| Structure | Raw blocks | Hierarchy | Flat (key-value) |

### Memory Trick
- **Block** = **B**asic building blocks (raw, fast)
- **File** = **F**olders and files (organized)
- **Object** = **O**cean of objects (unlimited, flat)

### Real Example: Instagram
- Profile data: Block storage (database)
- Application code: File storage
- Photos and videos: Object storage (S3)
- Thumbnails: Object storage + CDN

### Today's Quiz
1. Where would Netflix store its movies?
2. Why is object storage cheapest?
3. Can you edit part of an object in blob storage?

---

## DAY 28: Content Delivery & Streaming

### The Big Idea
Streaming is like drinking from a **water fountain** - you consume as the water flows. Downloading is like filling a bottle first, then drinking.

### Streaming vs Downloading
```
Downloading: [Full video file transfers] ----> [Then you watch]
Streaming:   [Small chunks transfer] --> [Watch immediately while more loads]
```

### How Video Streaming Works (Netflix/YouTube)
1. Video is split into small chunks (2-10 seconds each)
2. Each chunk is encoded in different qualities (360p, 720p, 1080p, 4K)
3. Your player requests chunks one by one
4. If internet is slow -> switch to lower quality
5. This is called **Adaptive Bitrate Streaming**

### Protocols for Streaming
- **HLS** (HTTP Live Streaming) - Apple's standard
- **DASH** (Dynamic Adaptive Streaming over HTTP) - Open standard
- **WebRTC** - Real-time (video calls)

### CDN + Streaming
```
[Origin: Full video] --> Distributed to CDN edges worldwide
User in Tokyo gets video from Tokyo edge (not US origin)
Result: Fast loading, less buffering!
```

### Memory Trick
**STREAM = Serves Tiny Rounds of Entertainment And Media**

### Video Processing Pipeline (YouTube)
```
Upload --> [Transcoding: convert to multiple formats]
       --> [Quality: 360p, 720p, 1080p, 4K]
       --> [Chunking: split into 5-sec pieces]
       --> [Store in Object Storage]
       --> [Distribute to CDN]
       --> [User streams from nearest CDN]
```

### Today's Quiz
1. Why does video quality change while watching Netflix?
2. What's the benefit of splitting video into chunks?
3. Why is WebRTC used for video calls but not Netflix?

---


## DAY 29: Distributed Systems Fundamentals

### The Big Idea
A distributed system is a group of computers working together that appears as **one system** to the user. Like a restaurant chain - you go to any location and get the same food, but behind the scenes, many kitchens are coordinating!

### Why Distributed Systems?
1. No single computer is powerful enough
2. Users are spread around the world
3. Need to survive failures
4. Need to handle massive scale

### Key Challenges

**1. Network Failures**
- Computers communicate over networks
- Networks can be slow, drop messages, or die
- You MUST design for network failure

**2. Clock Synchronization**
- Different computers have slightly different clocks
- "What time did this happen?" is surprisingly hard
- Solution: Logical clocks (Lamport timestamps)

**3. Split Brain**
- Network splits into two groups
- Each group thinks the other is dead
- Both might try to be "master" -> conflicts!

### Consensus Problem
How do multiple computers agree on something?
Like: 5 friends trying to decide where to eat, but they can only text (and texts might not deliver)

**Popular Solution: Raft Algorithm**
- One node is elected "leader"
- Leader makes decisions
- Others follow the leader
- If leader dies, election happens!

### Memory Trick
**DISTRIBUTED = Dozens of Independent Systems Together Running In Better Unison Than Expected, Delivering**

### The Two Generals Problem
```
General A wants to attack with General B.
They send messengers through enemy territory.
Problem: How do they BOTH know the other got the message?
Surprise: This is IMPOSSIBLE to solve perfectly!
```

This is why distributed systems are fundamentally hard.

### Today's Quiz
1. What is the "split brain" problem?
2. Why can't we just use wall clocks in distributed systems?
3. How does the Raft algorithm handle leader failure?

---

## DAY 30: Leader Election & Coordination

### The Big Idea
In a group of servers, sometimes ONE server needs to be the "boss" (leader). Leader election is the process of choosing that boss - fairly and automatically!

### Why Do We Need a Leader?
- Someone needs to make final decisions
- Someone coordinates writes
- Someone assigns tasks to workers
- Avoid conflicts (two servers doing the same job)

### How Leader Election Works

**1. Bully Algorithm**
```
All servers have IDs: [1, 2, 3, 4, 5]
- Highest living ID = Leader
- Server 5 is leader
- Server 5 dies
- Servers 1-4 notice
- Server 4 says "I'm the new leader!" (highest alive)
- Like the tallest person in the room is captain
```

**2. Raft Consensus**
```
- Servers start as "followers"
- If no heartbeat from leader for X seconds...
- A follower becomes "candidate" and asks for votes
- If majority votes yes -> New leader!
- Like a class electing a president
```

### ZooKeeper - The Coordination King
ZooKeeper is like a **shared notebook** that all servers trust:
- Who is the current leader? (Check the notebook)
- Which servers are alive? (They sign in)
- What's the current configuration? (Written in notebook)

```
[Server 1] --\
[Server 2] ----> [ZooKeeper] <-- Source of truth
[Server 3] --/
```

### Memory Trick
**Leader = The One Everyone Agrees To Listen To**
- Not the strongest, not the smartest
- Just the one everyone AGREES on!

### Real Examples
- **Kafka**: Uses ZooKeeper for leader election of partitions
- **Elasticsearch**: Elects a master node
- **etcd**: Used by Kubernetes for coordination

### Today's Quiz
1. What happens if the leader dies?
2. Why do we need consensus for leader election?
3. What is ZooKeeper used for?

---

## DAY 31: Event-Driven Architecture

### The Big Idea
Instead of services ASKING each other for updates, they ANNOUNCE events and whoever cares listens. Like a school PA system - the announcement goes out, and only relevant people act on it!

### Request-Driven vs Event-Driven
```
Request-Driven (Traditional):
Order Service: "Hey Inventory, reduce stock!"
Order Service: "Hey Email, send confirmation!"
Order Service: "Hey Analytics, log this!"
(Order service knows about everyone - tightly coupled)

Event-Driven:
Order Service: "ORDER_PLACED!" (announces to everyone)
Inventory: "I heard! Reducing stock."
Email: "I heard! Sending confirmation."
Analytics: "I heard! Logging it."
(Order service doesn't know or care who listens!)
```

### Key Concepts

**Event**: Something that happened ("user_signed_up", "order_placed")
**Producer**: Creates events (publishes)
**Consumer**: Listens for events (subscribes)
**Event Bus/Broker**: The channel events flow through

### Event Patterns

**1. Pub/Sub (Publish-Subscribe)**
```
[Producer] --> [Topic: "orders"] --> [Consumer 1: Email]
                                 --> [Consumer 2: Inventory]
                                 --> [Consumer 3: Analytics]
All consumers get the same event!
```

**2. Event Sourcing**
- Store ALL events, not just current state
- Like a bank statement (list of transactions, not just balance)
- Can replay events to rebuild state!

```
Event Log:
1. Account Created (balance: 0)
2. Deposit $100 (balance: 100)
3. Withdraw $30 (balance: 70)
4. Deposit $50 (balance: 120)
Current state = replay all events!
```

### Memory Trick
**EVENT = Everything Ventures Effortlessly, Notifying Things**

### Benefits
1. **Loose coupling**: Services don't know about each other
2. **Scalability**: Add new consumers without changing producers
3. **Audit trail**: All events are recorded
4. **Replay**: Can reprocess past events

### Today's Quiz
1. Why is event-driven architecture more scalable?
2. What's the difference between Pub/Sub and a message queue?
3. How would you use event sourcing for a bank account?

---


## DAY 32: Search Systems & Indexing

### The Big Idea
How does Google search billions of web pages in 0.5 seconds? The secret is **inverted indexes** - like the index at the back of a book, but for the entire internet!

### How Search Works

**1. Crawling** - Discover pages (like exploring every street in a city)
**2. Indexing** - Organize what you found (like creating a card catalog)
**3. Ranking** - Decide what's most relevant (like sorting best to worst)

### Inverted Index
Normal: Document -> Words
```
Doc 1: "The cat sat on the mat"
Doc 2: "The dog sat on the log"
```

Inverted: Word -> Documents
```
"cat" -> [Doc 1]
"sat" -> [Doc 1, Doc 2]
"dog" -> [Doc 2]
"the" -> [Doc 1, Doc 2]
```

Now searching for "cat" instantly gives you Doc 1!

### Elasticsearch - The Search Engine
- Built on Apache Lucene
- Distributed (spreads across many servers)
- Near real-time search
- Used by: Wikipedia, GitHub, Netflix

### How to Design a Search System
```
[User types query] --> [Query Parser]
                          |
                    [Inverted Index]
                          |
                    [Ranking Algorithm]
                          |
                    [Return Top Results]
```

### Memory Trick
**Think of search like a library:**
- **Without index**: Walk through every shelf, check every book
- **With index**: Look up the card catalog, go directly to the book

### Relevance Ranking (TF-IDF)
- **TF (Term Frequency)**: How often the word appears in this document
- **IDF (Inverse Document Frequency)**: How rare the word is across all documents
- Rare words in a document = more relevant!

### Today's Quiz
1. What is an inverted index?
2. Why is "the" a bad search term?
3. How would you design search for an e-commerce site?

---

## DAY 33: Data Partitioning Strategies

### The Big Idea
When your data is too big for one machine, you split it across multiple machines. The question is HOW to split it smartly!

### Partitioning Strategies

**1. Horizontal Partitioning (Sharding)**
- Split rows across machines
- Each machine has ALL columns but SOME rows
```
Machine 1: Users A-M
Machine 2: Users N-Z
```

**2. Vertical Partitioning**
- Split columns across machines
- Each machine has ALL rows but SOME columns
```
Machine 1: user_id, name, email (frequently accessed)
Machine 2: user_id, bio, preferences (rarely accessed)
```

**3. Functional Partitioning**
- Split by function/feature
- Each machine handles a different type of data
```
Machine 1: User data
Machine 2: Product data
Machine 3: Order data
```

### Choosing a Partition Key
The partition key determines WHERE data goes. Choose wisely!

**Good Partition Key:**
- Evenly distributes data
- Queries mostly hit ONE partition
- Example: user_id (each user's data on one machine)

**Bad Partition Key:**
- Creates hotspots (uneven distribution)
- Example: country (US might have 70% of users)
- Example: date (today's partition gets ALL traffic)

### Memory Trick
**Partition = Pizza slicing**
- **Horizontal** = Cut into rows (like cutting a pizza in strips)
- **Vertical** = Cut into columns (like cutting pizza in wedges)
- **Functional** = Different pizzas for different tables

### Hotspot Problem & Solutions
Problem: One partition gets way more traffic
Solutions:
1. Add randomness to key (append random digit)
2. Split hot partitions further
3. Use consistent hashing with virtual nodes

### Today's Quiz
1. What's the difference between horizontal and vertical partitioning?
2. Why is "date" often a bad partition key?
3. Design a partition strategy for Twitter's tweets.

---

## DAY 34: Batch vs Stream Processing

### The Big Idea
- **Batch Processing** = Washing clothes once a week (collect all, process together)
- **Stream Processing** = Assembly line at a factory (process each item as it arrives)

### Batch Processing
```
Collect data --> Wait until there's a lot --> Process all at once
```
- Example: Netflix generating "recommended for you" overnight
- Example: Monthly bank statements
- Example: Daily sales reports

**Tools**: Hadoop, Apache Spark, AWS Batch

### Stream Processing
```
Data arrives --> Process immediately --> Results in real-time
```
- Example: Fraud detection (block suspicious transaction instantly)
- Example: Live traffic updates on Google Maps
- Example: Real-time sports scores

**Tools**: Apache Kafka Streams, Apache Flink, Apache Storm

### Comparison
| Feature | Batch | Stream |
|---------|-------|--------|
| When processed | Later (scheduled) | Immediately |
| Latency | Minutes to hours | Milliseconds to seconds |
| Data size | Very large | One event at a time |
| Complexity | Simpler | More complex |
| Use case | Reports, ML training | Alerts, real-time dashboards |

### Lambda Architecture (Best of Both!)
```
[Data] --> [Batch Layer: Process ALL historical data] --> [Batch View]
   |                                                          |
   +--> [Speed Layer: Process REAL-TIME data]  --> [Real-time View]
                                                          |
                            [Query: Merge batch + real-time views]
```

### Memory Trick
- **Batch** = **B**ig pile, process later (like laundry day)
- **Stream** = **S**traight through, no waiting (like conveyor belt)

### Today's Quiz
1. Should fraud detection use batch or stream processing?
2. Why might you need BOTH batch and stream?
3. Name 3 real-world stream processing use cases.

---


## DAY 35: API Gateway Pattern

### The Big Idea
An API Gateway is like the **front desk of a hotel**. Guests don't go directly to housekeeping, restaurant, or maintenance. They tell the front desk what they need, and the front desk routes them!

### Without API Gateway
```
Mobile App must know about:
- User Service (port 3001)
- Payment Service (port 3002)
- Order Service (port 3003)
- Notification Service (port 3004)
Complex! What if services move?
```

### With API Gateway
```
Mobile App --> [API Gateway] --> User Service
                             --> Payment Service
                             --> Order Service
                             --> Notification Service
App only knows ONE address!
```

### What API Gateway Does
1. **Routing**: Directs requests to correct service
2. **Authentication**: Checks if user is logged in
3. **Rate Limiting**: Prevents abuse
4. **Load Balancing**: Spreads traffic
5. **Caching**: Returns cached responses
6. **Request/Response Transformation**: Converts formats
7. **Monitoring**: Tracks all API calls

### Memory Trick
**API Gateway = AIRPORT**
- Single entry point (front door)
- Security check (authentication)
- Directs you to correct gate (routing)
- Controls flow of people (rate limiting)

### Popular API Gateways
- **Kong** - Open source, very popular
- **AWS API Gateway** - Managed by Amazon
- **Nginx** - Can act as API gateway
- **Zuul** - Netflix's gateway

### BFF Pattern (Backend for Frontend)
Different clients need different data:
```
[Mobile App] --> [Mobile BFF] --> [Microservices]
[Web App]    --> [Web BFF]    --> [Microservices]
[TV App]     --> [TV BFF]     --> [Microservices]
```
Each BFF is customized for its client!

### Today's Quiz
1. What are 3 responsibilities of an API Gateway?
2. Why would a mobile app need different data than a web app?
3. What happens if the API Gateway goes down?

---

## DAY 36: Database Types Deep Dive

### The Big Idea
Different databases are like different vehicles - a bus, car, motorcycle, and bicycle. Each is best for different situations!

### Database Types

**1. Relational (SQL)**
- Tables with rows and columns
- Best for: Structured data, complex queries
- Examples: PostgreSQL, MySQL, Oracle
- Use when: Banking, e-commerce, ERP systems

**2. Document (NoSQL)**
- JSON-like documents
- Best for: Flexible schemas, rapid development
- Examples: MongoDB, CouchDB
- Use when: User profiles, content management, catalogs

**3. Key-Value**
- Simple: key -> value pairs
- Best for: Caching, sessions, simple lookups
- Examples: Redis, DynamoDB, Memcached
- Use when: Shopping carts, user sessions, leaderboards

**4. Wide-Column**
- Tables but columns can vary per row
- Best for: Time-series, IoT data, huge datasets
- Examples: Cassandra, HBase, ScyllaDB
- Use when: Sensor data, log analysis, messaging

**5. Graph**
- Nodes and relationships
- Best for: Connected data, social networks
- Examples: Neo4j, Amazon Neptune
- Use when: Social graphs, recommendation engines, fraud detection

**6. Time-Series**
- Optimized for timestamp-based data
- Best for: Metrics, monitoring, IoT
- Examples: InfluxDB, TimescaleDB, Prometheus

### Decision Matrix
| Need | Best Database Type |
|------|-------------------|
| Complex queries with joins | SQL (PostgreSQL) |
| Flexible JSON documents | Document (MongoDB) |
| Lightning-fast lookups | Key-Value (Redis) |
| Social connections | Graph (Neo4j) |
| Metrics over time | Time-Series (InfluxDB) |
| Massive write throughput | Wide-Column (Cassandra) |

### Memory Trick
**Pick database like picking a vehicle:**
- Need precision? SQL (luxury car)
- Need flexibility? Document (SUV)
- Need speed? Key-Value (sports car)
- Need connections? Graph (subway map)

### Today's Quiz
1. What database would you choose for a recommendation engine?
2. Why would you use a time-series database for server monitoring?
3. Can you use multiple database types in one system?

---

## DAY 37: Idempotency & Retry Mechanisms

### The Big Idea
**Idempotent** means doing something multiple times has the SAME effect as doing it once. Like pressing an elevator button - pressing it 5 times doesn't make the elevator come 5 times faster!

### Why Idempotency Matters
```
Scenario: You click "Pay $100" button
Network glitch: Your phone doesn't get the response
Phone retries: Sends payment request again
WITHOUT idempotency: You get charged $200!
WITH idempotency: You get charged $100 (second request is ignored)
```

### Idempotent vs Non-Idempotent
| Operation | Idempotent? | Why |
|-----------|------------|-----|
| GET /users/123 | Yes | Reading doesn't change anything |
| DELETE /users/123 | Yes | Deleting twice = same as once |
| PUT /users/123 {name: "Bob"} | Yes | Setting to same value repeatedly |
| POST /orders | NO! | Creates new order each time |
| POST /payments | Must make it so! | Use idempotency key |

### How to Make Operations Idempotent
**1. Idempotency Key**
```
Client sends: POST /payment {amount: 100, idempotency_key: "abc123"}
Server checks: Have I seen "abc123" before?
  - No: Process payment, store key
  - Yes: Return previous result (don't charge again!)
```

**2. Database Constraints**
```sql
-- Unique constraint prevents duplicates
INSERT INTO payments (id, amount, user_id)
VALUES ('abc123', 100, 456)
ON CONFLICT (id) DO NOTHING;
```

### Retry Strategies

**1. Simple Retry**
- Try again immediately
- Problem: If server is overloaded, this makes it worse!

**2. Exponential Backoff**
```
Attempt 1: Wait 1 second
Attempt 2: Wait 2 seconds
Attempt 3: Wait 4 seconds
Attempt 4: Wait 8 seconds
(Doubles each time!)
```

**3. Exponential Backoff with Jitter**
- Add random time to avoid all clients retrying simultaneously
- Attempt 1: 1s + random(0-0.5s)
- Attempt 2: 2s + random(0-1s)

### Memory Trick
**IDEMPOTENT = I Do Everything More than once but the outcome remains the same regardless of my Patience of ENTering it multiple Times**

### Today's Quiz
1. Is "transfer $50 from A to B" idempotent? How would you make it so?
2. Why is exponential backoff better than immediate retry?
3. What is "jitter" and why do we need it?

---


## DAY 38: Circuit Breaker Pattern

### The Big Idea
A circuit breaker in software works like a **circuit breaker in your home**. When there's an electrical problem, it trips and cuts power to prevent fire. In software, it stops calling a failing service to prevent cascading failures!

### The Problem
```
Service A calls Service B.
Service B is down.
Without circuit breaker:
  Service A keeps trying... waiting... timing out... 
  Service A gets slow...
  Service C (which depends on A) gets slow too...
  EVERYTHING cascades and crashes!
```

### Circuit Breaker States
```
[CLOSED] -- too many failures --> [OPEN] -- timeout expires --> [HALF-OPEN]
   |                                |                              |
   | Normal operation               | Reject all requests          | Allow few test requests
   | Requests pass through          | Return error immediately     |
   |                                |                              |
   | <-- success -- [HALF-OPEN] -- if tests pass --> back to CLOSED
                                   -- if tests fail --> back to OPEN
```

**CLOSED** (Normal):
- Everything working fine
- Requests pass through
- Count failures

**OPEN** (Protection mode):
- Too many failures detected!
- Reject requests immediately (don't even try)
- Wait for timeout period

**HALF-OPEN** (Testing):
- After timeout, try a few requests
- If they succeed -> CLOSE (back to normal!)
- If they fail -> OPEN again (still broken)

### Memory Trick
**Like a doctor:**
- CLOSED = Patient is healthy, normal activities
- OPEN = Patient is sick, bed rest (no activities)
- HALF-OPEN = Patient trying light exercise (testing if better)

### Real Example: Netflix
- Netflix has 700+ microservices
- If one dies, circuit breaker prevents cascade
- Instead of waiting, show cached/default content
- "Sorry, recommendations unavailable" is better than entire Netflix down!

### Settings to Configure
- **Failure threshold**: How many failures before opening? (e.g., 5 failures)
- **Timeout**: How long to stay open? (e.g., 30 seconds)
- **Success threshold**: How many successes in half-open to close? (e.g., 3 successes)

### Today's Quiz
1. What happens in the HALF-OPEN state?
2. Why is "fail fast" better than "wait and timeout"?
3. How does Netflix use circuit breakers?

---

## DAY 39: Saga Pattern - Distributed Transactions

### The Big Idea
In microservices, a single business transaction might span multiple services. If one step fails, you need to UNDO all previous steps. A Saga manages this!

### The Problem
```
Booking a Trip:
1. Book Flight ✓
2. Book Hotel ✓
3. Book Car ✗ (FAILED!)

Now what? Need to cancel flight AND hotel!
```

In a monolith, you'd use database transactions (rollback).
In microservices, services have SEPARATE databases - can't rollback!

### Saga Solution
Each step has a **compensating action** (undo):
```
Step 1: Book Flight    | Undo: Cancel Flight
Step 2: Book Hotel     | Undo: Cancel Hotel
Step 3: Book Car       | Undo: Cancel Car

If Step 3 fails:
  - Run Undo for Step 2 (Cancel Hotel)
  - Run Undo for Step 1 (Cancel Flight)
```

### Two Saga Approaches

**1. Choreography (No central coordinator)**
```
Services communicate through events:
Flight: "Flight Booked!" --> Hotel hears, books hotel
Hotel: "Hotel Booked!" --> Car hears, tries to book car
Car: "Car Failed!" --> Hotel hears, cancels hotel
Hotel: "Hotel Cancelled!" --> Flight hears, cancels flight
```
Like a dance where everyone knows their part!

**2. Orchestration (Central coordinator)**
```
[Saga Orchestrator]
  --> "Book flight" --> Flight Service: "Done!"
  --> "Book hotel" --> Hotel Service: "Done!"
  --> "Book car" --> Car Service: "Failed!"
  --> "Cancel hotel" --> Hotel Service: "Cancelled!"
  --> "Cancel flight" --> Flight Service: "Cancelled!"
```
Like a conductor leading an orchestra!

### Memory Trick
- **Choreography** = Everyone dances on their own (no director)
- **Orchestration** = One conductor tells everyone what to play

### Real Example: E-commerce Order
```
1. Reserve Inventory | Undo: Release Inventory
2. Process Payment   | Undo: Refund Payment
3. Ship Order        | Undo: Cancel Shipment
4. Send Confirmation | Undo: Send Cancellation Email
```

### Today's Quiz
1. When would you use Choreography vs Orchestration?
2. What is a compensating transaction?
3. Design a saga for a money transfer between two banks.

---

## DAY 40: System Design Trade-offs Summary

### The Big Idea
System design is ALL about trade-offs. There's never a perfect solution - only the BEST solution for YOUR specific situation!

### Key Trade-offs

**1. Consistency vs Availability (CAP)**
- Strong consistency = Slower but accurate
- High availability = Faster but might be stale

**2. Latency vs Throughput**
- Optimize for speed of individual request?
- Or optimize for total requests handled?

**3. SQL vs NoSQL**
- Structure & ACID vs Flexibility & Speed

**4. Monolith vs Microservices**
- Simplicity vs Scalability

**5. Batch vs Real-time**
- Efficiency vs Immediacy

**6. Cache vs Freshness**
- Speed vs Accuracy (cached data might be old)

**7. Replication vs Cost**
- More copies = More safety but more expensive

**8. Simplicity vs Performance**
- Simple code that's maintainable vs Complex optimized code

### The Golden Rule of Trade-offs
**Always ask: "What are we optimizing for?"**
- Social media: Optimize for availability
- Banking: Optimize for consistency
- Gaming: Optimize for latency
- Big data: Optimize for throughput

### Memory Trick
**TRADE = Think Really About Design Extremes**
Every choice has a cost. Know what you're paying!

### Phase 2 Checklist
- [ ] Availability & Reliability
- [ ] Consistency Patterns
- [ ] Hashing & Checksums
- [ ] WebSockets & Real-Time
- [ ] Authentication & Authorization
- [ ] Logging, Monitoring & Alerting
- [ ] Storage Systems
- [ ] Streaming & Content Delivery
- [ ] Distributed Systems
- [ ] Leader Election
- [ ] Event-Driven Architecture
- [ ] Search Systems
- [ ] Data Partitioning
- [ ] Batch vs Stream Processing
- [ ] API Gateway
- [ ] Database Types
- [ ] Idempotency & Retries
- [ ] Circuit Breaker
- [ ] Saga Pattern
- [ ] Trade-offs

---

# MINI PROJECT: Design a Food Delivery System
Design a system like UberEats/DoorDash with:
- User browses restaurants and menus
- User places order and pays
- Restaurant accepts order and prepares food
- Driver is assigned and picks up food
- Real-time tracking of delivery
- Rating system after delivery

Identify: Which databases? Which patterns? What trade-offs?

---


---

# PHASE 3: BUILDING BLOCKS (Days 41-60)
## Components & Design Patterns

---

## DAY 41: Unique ID Generation

### The Big Idea
Every item in a system needs a unique ID (like your social security number). But in a distributed system with billions of items, how do you make sure no two things get the same ID?

### The Challenge
- Multiple servers creating IDs simultaneously
- Need to be unique across ALL servers
- Need to be fast (can't check against all existing IDs)
- Sometimes need to be sortable by time

### Solutions

**1. UUID (Universally Unique Identifier)**
```
Example: 550e8400-e29b-41d4-a716-446655440000
- 128 bits, extremely unlikely to collide
- No coordination needed between servers
- Problem: Long, not sortable, bad for database indexes
```

**2. Auto-Increment with Database**
```
Server 1: IDs = 1, 3, 5, 7... (odd numbers)
Server 2: IDs = 2, 4, 6, 8... (even numbers)
- Simple but limited to how many servers
- Need coordination
```

**3. Twitter's Snowflake ID**
```
64-bit ID structure:
| 1 bit unused | 41 bits timestamp | 10 bits machine ID | 12 bits sequence |

- Timestamp: milliseconds (gives ~69 years)
- Machine ID: which server (1024 machines)
- Sequence: counter per millisecond (4096 per ms per machine)
- SORTABLE! IDs created later have higher values
- Each machine generates independently!
```

**4. Instagram's ID**
```
- Similar to Snowflake
- 41 bits: timestamp in milliseconds
- 13 bits: shard ID (which database)
- 10 bits: auto-incrementing sequence
```

### Memory Trick
**SNOWFLAKE = Sorted, No collisions, Organized With Fast Local Assignment, Known Everywhere**

### Which to Choose?
| Need | Best Choice |
|------|------------|
| Simple, any size | UUID |
| Sortable, fast | Snowflake |
| Human-readable | Custom (like "USR-001") |
| Super compact | Auto-increment (if single DB) |

### Today's Quiz
1. Why can't you just use auto-increment in distributed systems?
2. What makes Snowflake IDs sortable?
3. Design an ID system for a social media app with 10,000 posts/second.

---

## DAY 42: Bloom Filters - Probably Yes, Definitely No

### The Big Idea
A Bloom Filter is a space-efficient data structure that tells you:
- "Definitely NOT in the set" (100% sure)
- "PROBABLY in the set" (might be wrong)

Like a bouncer who might accidentally let a stranger in, but NEVER keeps a VIP out!

### How It Works
```
1. Create a bit array of size m (all zeros): [0,0,0,0,0,0,0,0,0,0]

2. To ADD "apple":
   hash1("apple") = 3, hash2("apple") = 7
   Set bits 3 and 7: [0,0,0,1,0,0,0,1,0,0]

3. To ADD "banana":
   hash1("banana") = 1, hash2("banana") = 7
   Set bits 1 and 7: [0,1,0,1,0,0,0,1,0,0]

4. To CHECK "cherry":
   hash1("cherry") = 3, hash2("cherry") = 5
   Bit 3 = 1 ✓, Bit 5 = 0 ✗
   Result: DEFINITELY NOT in set!

5. To CHECK "apple":
   hash1("apple") = 3, hash2("apple") = 7
   Bit 3 = 1 ✓, Bit 7 = 1 ✓
   Result: PROBABLY in set (might be false positive)
```

### Real Use Cases
- **Google Chrome**: Is this URL malicious? (Check bloom filter before expensive lookup)
- **Databases**: Is this key in this file? (Avoid reading disk if definitely not)
- **CDN**: Has this content been cached? 
- **Social media**: Has this user seen this post?

### Memory Trick
**BLOOM = Blocks Lookups On Obviously Missing data**

### Trade-offs
- Pro: Very memory efficient (1 bit per element vs storing actual data)
- Pro: O(1) lookup time (constant speed)
- Con: False positives possible
- Con: Can't delete elements (or use Counting Bloom Filter)

### Today's Quiz
1. Can a Bloom Filter give false negatives?
2. Why is a Bloom Filter used before database lookups?
3. What happens to accuracy as you add more elements?

---

## DAY 43: Geospatial Indexing - Location-Based Systems

### The Big Idea
How does Uber find the nearest drivers? How does Google Maps show restaurants near you? The answer: **Geospatial Indexing** - special ways to organize location data!

### The Problem
You're at location (40.7, -74.0) and want to find all restaurants within 1 mile.
Checking ALL restaurants in the database = TOO SLOW!

### Solutions

**1. Geohashing**
Converts location to a string:
```
(40.748817, -73.985428) --> "dr5ru7"
Nearby locations share the same PREFIX!
"dr5ru7" and "dr5ru6" are neighbors!
```
Like a zip code but more precise:
- "d" = continent
- "dr" = region  
- "dr5" = city area
- "dr5r" = neighborhood
- "dr5ru" = block
- "dr5ru7" = exact spot

**2. Quadtree**
Split the world into 4 quadrants recursively:
```
[World]
├── [NW quarter]
│   ├── [NW-NW] (few items, stop splitting)
│   └── [NW-SE] (many items, keep splitting...)
├── [NE quarter]
├── [SW quarter]
└── [SE quarter]
```
Dense areas get split more = more precision where needed!

**3. R-Tree**
- Groups nearby objects in bounding boxes
- Used in PostGIS (PostgreSQL extension)
- Great for: "Find all restaurants in this rectangle"

### Memory Trick
**GEO = Grids Enable Ordering (of locations)**

### Real Examples
- **Uber**: Geohash to find nearby drivers
- **Tinder**: Geohash to find nearby users
- **DoorDash**: Quadtree to find nearby restaurants
- **Google Maps**: R-tree for map rendering

### Today's Quiz
1. Why is geohashing fast for "nearby" queries?
2. When would you choose Quadtree over Geohash?
3. Design a system to find the 5 nearest gas stations.

---


## DAY 44: Counters at Scale

### The Big Idea
Counting sounds simple, right? But what if 100,000 people "like" a post at the SAME SECOND? A simple counter would break! Let's learn how to count at massive scale.

### The Problem
```
Post has 999,999 likes.
1000 people click "like" simultaneously.
Without careful design: All read 999,999 and write 1,000,000
Result: 1,000,000 instead of 1,000,999!
```

### Solutions

**1. Atomic Operations**
```
Instead of: READ count, ADD 1, WRITE new count
Do: INCREMENT count BY 1 (single atomic operation)
Database handles the locking!
Redis: INCR likes:post123
```

**2. Sharded Counters**
- Split one counter into many sub-counters
- Each sub-counter handles a portion of increments
```
Total Likes = counter_1 + counter_2 + counter_3 + counter_4
Counter 1: 250,000
Counter 2: 250,333
Counter 3: 250,100
Counter 4: 250,566
Total: ~1,000,999
```
- Reduces contention (less fighting over one number)!

**3. Approximate Counting (HyperLogLog)**
- When exact count doesn't matter
- Uses very little memory
- Example: "This post has ~1M views" (not exactly 1,000,247)
- Redis: PFADD and PFCOUNT

### Memory Trick
**Think of counting like voting:**
- Atomic = One ballot box, everyone waits in line
- Sharded = Multiple ballot boxes, faster!
- Approximate = Exit polls (close enough)

### Real Examples
- **YouTube view count**: Eventually consistent (shows "1.2M views" not exact)
- **Twitter like count**: Sharded counters
- **Reddit upvotes**: Cached and periodically synced

### Today's Quiz
1. Why is a simple counter problematic at scale?
2. When would you use approximate counting?
3. Design a view counter for a video platform with 1M concurrent viewers.

---

## DAY 45: Notification Systems

### The Big Idea
Notifications are like a **postal service** that delivers different types of messages through different channels. Design it wrong, and users either get spammed or miss important alerts!

### Types of Notifications
1. **Push Notifications** (mobile) - "Someone liked your post"
2. **SMS** - "Your OTP is 123456"
3. **Email** - "Your order has shipped"
4. **In-App** - Badge count, notification bell
5. **WebSocket** - Real-time alerts in browser

### High-Level Architecture
```
[Event Happens] --> [Notification Service] --> [Priority Queue]
                                                     |
                    +--------------------+-----------+-----------+
                    |                    |           |           |
              [Push Service]    [SMS Gateway]  [Email Service] [In-App]
                    |                    |           |           |
              [Apple/Google]     [Twilio]     [SendGrid]   [WebSocket]
                    |                    |           |           |
              [User's Phone]    [User's Phone] [User's Email] [User's Browser]
```

### Key Design Decisions

**1. User Preferences**
- User chooses: Email? Push? Both?
- Quiet hours: No notifications 10PM - 8AM

**2. Rate Limiting**
- Max 10 push notifications per hour
- Batch similar notifications: "5 people liked your post" (not 5 separate ones)

**3. Priority**
- Critical: OTP, security alerts (send immediately)
- High: Messages from friends
- Low: Marketing, recommendations (can wait)

**4. Retry Logic**
- Push failed? Try again in 5 seconds
- After 3 failures? Switch to SMS or email

### Memory Trick
**NOTIFY = Never Overwhelm, Target Intelligently, Filter Yourself**

### Today's Quiz
1. Why do you need a priority queue for notifications?
2. How would you handle a user who has 5 devices?
3. Design a notification system for a banking app.

---

## DAY 46: Distributed Locking

### The Big Idea
In a distributed system, multiple servers might try to do the same thing at the same time. A distributed lock is like a **bathroom key** - only one person can have it at a time!

### Why We Need Distributed Locks
```
Without lock:
Server 1: Read inventory (10 items) -> Sell 1 -> Write (9 items)
Server 2: Read inventory (10 items) -> Sell 1 -> Write (9 items)
Result: 9 items left, but sold 2! Should be 8!

With lock:
Server 1: LOCK -> Read (10) -> Sell -> Write (9) -> UNLOCK
Server 2: Wait... LOCK -> Read (9) -> Sell -> Write (8) -> UNLOCK
Result: Correct! 8 items left.
```

### Implementation with Redis (Redlock)
```
1. Server tries to acquire lock:
   SET lock:inventory "server1" NX PX 30000
   (Set only if Not eXists, expires in 30 seconds)

2. If successful: Do your work, then DELETE lock
3. If failed: Someone else has the lock, wait and retry
4. Expiry: If server dies, lock auto-releases after 30 seconds!
```

### Common Issues

**1. Lock Expires Too Early**
- Server takes too long, lock expires, another server gets in
- Solution: Renew lock periodically (like refreshing a parking meter)

**2. Server Dies While Holding Lock**
- Lock never released, everyone waits forever
- Solution: TTL (Time To Live) - lock auto-expires

**3. Split Brain**
- Network split, two servers think they have the lock
- Solution: Use consensus (like Redlock with multiple Redis instances)

### Memory Trick
**LOCK = Let Only one Computer through the Key-hole**

### Alternatives to Locks
- **Optimistic Locking**: Don't lock, but check before writing (version numbers)
- **Database row locking**: Let DB handle it
- **Queue-based**: Process one at a time via queue

### Today's Quiz
1. Why does a lock need an expiry time?
2. What is the danger of a lock that's held too long?
3. How does Redlock work across multiple Redis instances?

---


## DAY 47: Data Rebalancing & Migration

### The Big Idea
As your system grows, you need to move data around - like reorganizing a library when it gets new sections. This is called rebalancing!

### When You Need to Rebalance
- Adding new database servers (shards)
- One shard is getting too full (hotspot)
- Upgrading hardware
- Geographic expansion

### Strategies

**1. Fixed Number of Partitions**
- Create MORE partitions than servers initially
- When adding a server, just move some partitions
```
Before: Server A [P1,P2,P3,P4,P5,P6] Server B [P7,P8,P9,P10,P11,P12]
After:  Server A [P1,P2,P3,P4] Server B [P7,P8,P9,P10] Server C [P5,P6,P11,P12]
```

**2. Dynamic Partitioning**
- Split a partition when it gets too big
- Merge small partitions together

**3. Proportional to Node Count**
- Each node gets a fixed number of partitions
- Adding a node redistributes evenly

### Data Migration Best Practices
1. **Double-Write**: Write to old AND new location during migration
2. **Backfill**: Copy historical data to new location
3. **Verify**: Compare old and new to ensure nothing was lost
4. **Switch**: Route traffic to new location
5. **Cleanup**: Remove old data after confidence period

### Memory Trick
**MIGRATE = Move Items Gradually, Replicating And Testing Everything**

### Today's Quiz
1. How do you avoid downtime during data migration?
2. What's the advantage of "fixed number of partitions"?
3. Design a migration plan for moving from one database to another.

---

## DAY 48: Gossip Protocol - How Nodes Share Information

### The Big Idea
Gossip Protocol works like actual gossip! Each node tells a few neighbors its news, who tell their neighbors, and soon everyone knows! No central coordinator needed.

### How It Works
```
Second 0: Node A has news "Node X is dead!"
Second 1: A tells B and C
Second 2: B tells D, C tells E
Second 3: D tells F, E tells G
... Soon ALL nodes know!
```

### Properties
- **Decentralized**: No single point of failure
- **Scalable**: Works with thousands of nodes
- **Eventually consistent**: Everyone knows eventually
- **Resilient**: Even if some messages are lost, gossip spreads

### Where It's Used
- **Cassandra**: Nodes discover each other and share state
- **DynamoDB**: Failure detection
- **Consul**: Service discovery
- **Bitcoin**: Transaction propagation

### Types of Information Shared
- Which nodes are alive/dead (failure detection)
- What data each node holds
- Load information (for balancing)

### Memory Trick
**GOSSIP = Gradually Observing System State In Parallel**
Like actual gossip: Tell 2 friends, they each tell 2 friends... exponential spread!

### Today's Quiz
1. Why is gossip protocol more resilient than a central coordinator?
2. How long does it take for gossip to reach all N nodes?
3. What's a disadvantage of gossip protocol?

---

## DAY 49: Service Discovery

### The Big Idea
In microservices, services need to FIND each other. It's like a phone book for services! Service Discovery answers: "Where is the Payment Service running right now?"

### The Problem
```
Order Service needs to call Payment Service.
But Payment Service might be at:
- 10.0.1.5:8080 (last week)
- 10.0.2.3:8080 (today - it moved!)
- Running on 3 instances now
How does Order Service know?
```

### Solutions

**1. Client-Side Discovery**
```
[Order Service] --> [Service Registry: "Payment is at 10.0.2.3"] --> [Payment Service]
Client asks registry, then connects directly.
```

**2. Server-Side Discovery**
```
[Order Service] --> [Load Balancer] --> [Payment Service]
Load balancer knows where services are.
Client doesn't need to know!
```

### Service Registry
A database of all services and their locations:
```
{
  "payment-service": [
    {"host": "10.0.2.3", "port": 8080, "health": "up"},
    {"host": "10.0.2.4", "port": 8080, "health": "up"},
    {"host": "10.0.2.5", "port": 8080, "health": "down"}
  ]
}
```

### Health Checks
- Services periodically say "I'm alive!" (heartbeat)
- If no heartbeat for X seconds, mark as dead
- Registry removes dead services from the list

### Tools
- **Consul** (HashiCorp) - Full service mesh
- **etcd** (CoreOS) - Key-value store for config
- **ZooKeeper** (Apache) - Coordination service
- **Kubernetes** - Built-in service discovery via DNS

### Memory Trick
**Service Discovery = The GPS of Microservices (finding what you need)**

### Today's Quiz
1. What happens if the Service Registry goes down?
2. Client-side vs Server-side discovery: pros and cons?
3. How do health checks prevent routing to dead services?

---

## DAY 50: Data Serialization Formats

### The Big Idea
When sending data between systems, you need to convert objects into bytes (serialize) and back (deserialize). Different formats have different trade-offs!

### Common Formats

**1. JSON (JavaScript Object Notation)**
```json
{"name": "Alice", "age": 25, "active": true}
```
- Human readable
- Widely supported
- Verbose (takes more space)
- Used in: REST APIs, config files

**2. Protocol Buffers (Protobuf) - by Google**
```protobuf
message User {
  string name = 1;
  int32 age = 2;
  bool active = 3;
}
```
- Binary format (not human readable)
- Very compact (3-10x smaller than JSON)
- Very fast to parse
- Schema required
- Used in: gRPC, internal services

**3. Apache Avro**
- Schema stored with data
- Good for data that evolves over time
- Used in: Hadoop, Kafka

**4. MessagePack**
- Like JSON but binary (smaller, faster)
- Drop-in replacement for JSON in many cases

### Comparison
| Format | Size | Speed | Human Readable | Schema Required |
|--------|------|-------|----------------|-----------------|
| JSON | Large | Slow | Yes | No |
| Protobuf | Small | Fast | No | Yes |
| Avro | Small | Fast | No | Yes |
| MessagePack | Medium | Medium | No | No |
| XML | Very Large | Slow | Yes | Optional |

### Memory Trick
- **JSON** = For humans (readable, everywhere)
- **Protobuf** = For machines (compact, fast)
- **Avro** = For evolution (schemas change over time)

### When to Use What
- Public APIs: JSON (everyone understands it)
- Internal microservices: Protobuf (fast, small)
- Data pipelines: Avro (schema evolution)
- Configuration: JSON or YAML (human editable)

### Today's Quiz
1. Why would you choose Protobuf over JSON for microservices?
2. What does "schema evolution" mean?
3. Why is JSON used for public APIs even though it's slower?

---


## DAY 51: Heartbeat & Failure Detection

### The Big Idea
In distributed systems, servers need to constantly say "I'm alive!" - like a heartbeat. If the heartbeat stops, other servers assume it's dead and take action!

### How It Works
```
Every 3 seconds:
Server A: "I'm alive!" --> Monitor
Server B: "I'm alive!" --> Monitor
Server C: "..........."  --> Monitor: "C hasn't responded for 9 seconds. C is DEAD!"
```

### Detection Strategies

**1. Push-based (Heartbeats)**
- Each server sends "I'm alive" periodically
- If no heartbeat for X time = assumed dead
- Simple but generates constant traffic

**2. Pull-based (Health Checks)**
- Monitor pings each server: "Are you alive?"
- Server responds or doesn't
- Less network traffic but slower detection

**3. Phi Accrual Failure Detector (Cassandra uses this)**
- Calculates PROBABILITY that a node is dead
- Adapts to network conditions
- Not binary (dead/alive) but a scale (probably dead/definitely dead)

### Avoiding False Positives
Problem: Server is alive but network was temporarily slow!
Solutions:
- Wait for multiple missed heartbeats (not just one)
- Use multiple monitors (majority must agree)
- Exponential backoff before declaring dead

### Memory Trick
**HEARTBEAT = How Each Application Reports That Beats Exist And Things work**

### What Happens After Detection
1. Remove dead server from load balancer rotation
2. Redirect traffic to healthy servers
3. Alert on-call engineers
4. Maybe replace with a new server (auto-healing)
5. If it was a database: Promote replica to master

### Today's Quiz
1. Why is one missed heartbeat not enough to declare a server dead?
2. What's the trade-off between quick detection and false positives?
3. Design a failure detection system for a 100-server cluster.

---

## DAY 52: Conflict Resolution

### The Big Idea
When multiple people edit the same data at the same time, you get conflicts! It's like two people trying to edit the same Google Doc paragraph simultaneously.

### Types of Conflicts
```
User A: Sets name to "Alice"    (at time T)
User B: Sets name to "Bob"      (at time T)
Both writes arrive at different replicas.
Which one wins?
```

### Resolution Strategies

**1. Last Write Wins (LWW)**
- Use timestamps: Latest write wins
- Simple but might lose valid data
- Used by: Cassandra, DynamoDB

**2. First Write Wins**
- First write is permanent, reject later ones
- Good for: Creating unique usernames

**3. Merge (CRDTs)**
- Conflict-free Replicated Data Types
- Automatically merge without conflicts
- Example: Counter CRDT (just add all increments!)
- Used by: Redis, Riak

**4. Application-Level Resolution**
- Let the user decide!
- Example: Google Docs shows both versions, user picks
- Example: Git merge conflicts

**5. Vector Clocks**
- Track history of who updated what
- Detect conflicts precisely
- Let application decide resolution

### Memory Trick
**CONFLICT = Cannot Offer Normal Fix; Let Intelligent Choice Triumph**

### Real Examples
- **Git**: Shows conflict markers, developer resolves
- **Google Docs**: Real-time merge with operational transforms
- **DynamoDB**: Last Write Wins with vector clocks for detection
- **Dropbox**: If conflict detected, create "conflicted copy"

### Today's Quiz
1. When is "Last Write Wins" dangerous?
2. How do CRDTs avoid conflicts entirely?
3. Design a conflict resolution system for a collaborative note-taking app.

---

## DAY 53: Back-of-the-Envelope Estimation

### The Big Idea
Before designing a system, you need to estimate its scale. How much storage? How many servers? How much bandwidth? Let's learn to calculate quickly!

### Key Numbers to Remember

**Data Sizes:**
- 1 character = 1 byte (ASCII) or 2-4 bytes (Unicode)
- Average tweet: ~300 bytes
- Average photo: 200KB - 2MB
- Average video (1 min): 50MB
- 1 Million = 10^6
- 1 Billion = 10^9

**Time:**
- 1 day = 86,400 seconds ≈ 100,000 seconds
- 1 month ≈ 2.5 million seconds
- 1 year ≈ 30 million seconds

**Scale:**
- 1 server handles ~1000-10,000 requests/second
- 1 database handles ~10,000-50,000 queries/second (read)
- SSD: 200MB/s read, 100MB/s write
- Network: 1 Gbps = 125 MB/s

### Example: Estimate Twitter's Storage

**Given:**
- 500 million tweets per day
- Average tweet: 300 bytes
- Store for 5 years

**Calculate:**
```
Daily storage = 500M × 300 bytes = 150 GB/day
Yearly storage = 150 GB × 365 = ~55 TB/year
5-year storage = 55 TB × 5 = ~275 TB

With replication (3 copies): 275 × 3 = ~825 TB ≈ 1 PB
```

### Example: Estimate Instagram's Bandwidth

**Given:**
- 100 million photo uploads per day
- Average photo: 1 MB
- Read-to-write ratio: 100:1

**Calculate:**
```
Write bandwidth = 100M × 1MB / 86400 sec = ~1.2 GB/s
Read bandwidth = 1.2 GB/s × 100 = ~120 GB/s
Need: 120 GB/s ÷ 0.125 GB/s per link = ~960 network links
```

### Memory Trick
**ESTIMATE = Every System Totally Involves Math, Approximation, And Thinking Extensively**

### Quick Estimation Tips
1. Round to powers of 2 or 10
2. Use back-of-napkin math (don't need calculator precision)
3. State assumptions clearly
4. Know: 1 million seconds ≈ 12 days

### Today's Quiz
1. Estimate storage for YouTube (500 hours of video uploaded per minute)
2. How many servers does a system need at 1 million requests/second?
3. Estimate the daily data generated by Uber rides globally.

---


## DAY 54: Connection Pooling

### The Big Idea
Creating a new database connection for every request is like building a new road for every car. Connection pooling keeps a set of ready-made connections that get reused. Like having a parking lot full of cars ready to go!

### The Problem
```
Without pooling:
Request 1: Open connection (50ms) -> Query (5ms) -> Close connection
Request 2: Open connection (50ms) -> Query (5ms) -> Close connection
Request 3: Open connection (50ms) -> Query (5ms) -> Close connection
Total: 165ms (most time spent opening connections!)

With pooling:
Request 1: Get connection from pool (0.1ms) -> Query (5ms) -> Return to pool
Request 2: Get connection from pool (0.1ms) -> Query (5ms) -> Return to pool
Request 3: Get connection from pool (0.1ms) -> Query (5ms) -> Return to pool
Total: 15.3ms (10x faster!)
```

### How It Works
```
[Application]
     |
[Connection Pool: 10 idle connections ready]
     |
[Database]

- Request comes in, borrow a connection
- Use it for the query
- Return it to the pool (don't close it!)
- Next request reuses same connection
```

### Key Settings
- **Min connections**: Always keep at least N connections ready
- **Max connections**: Never exceed N connections (prevent overload)
- **Idle timeout**: Close connections unused for X minutes
- **Max lifetime**: Replace connections after X hours (prevent stale)

### Memory Trick
**POOL = Pre-made, Open, On-demand Links (to the database)**

### Where Pooling Is Used
- Database connections (most common)
- HTTP connections (keep-alive)
- Thread pools (reuse threads)
- Object pools (expensive-to-create objects)

### Today's Quiz
1. Why is creating a new database connection expensive?
2. What happens when all connections in the pool are busy?
3. Why should connections have a "max lifetime"?

---

## DAY 55: CQRS - Command Query Responsibility Segregation

### The Big Idea
CQRS says: **Separate your READ operations from your WRITE operations.** Use different models (even different databases!) for reading and writing.

Like having separate doors at a bank: one for deposits (writes) and one for checking balance (reads).

### Why Separate?
- Reads and writes have DIFFERENT needs
- Reads: Fast, can be slightly stale, cacheable
- Writes: Must be accurate, validated, consistent
- Most systems are READ-heavy (90% reads, 10% writes)

### Traditional vs CQRS
```
Traditional:
[Client] --> [Single API] --> [Single Database]
(Same model for read and write)

CQRS:
[Client] --> [Write API] --> [Write DB (Normalized, PostgreSQL)]
                                    |
                              (Sync events)
                                    |
[Client] --> [Read API] --> [Read DB (Denormalized, Redis/Elasticsearch)]
```

### Example: E-commerce Product
```
Write Model (strict):
{
  "product_id": 123,
  "name": "Laptop",
  "price_cents": 99900,
  "stock": 50,
  "category_id": 7
}

Read Model (optimized for display):
{
  "product_id": 123,
  "name": "Laptop",
  "display_price": "$999.00",
  "in_stock": true,
  "category_name": "Electronics",
  "rating": 4.5,
  "review_count": 1247
}
```

### Memory Trick
**CQRS = Commands (write) Quarantined from Reads for Speed**

### When to Use CQRS
- Read-heavy systems (news feeds, catalogs)
- Complex read queries (dashboards, reports)
- Different scaling needs for reads vs writes

### When NOT to Use CQRS
- Simple CRUD applications
- Small teams (adds complexity)
- Data that must be instantly consistent

### Today's Quiz
1. Why optimize reads and writes separately?
2. What's the trade-off of CQRS? (hint: eventual consistency)
3. Design CQRS for a social media news feed.

---

## DAY 56: Reverse Index & Full-Text Search

### The Big Idea
How do you search through millions of documents in milliseconds? By pre-building a map from every word to every document that contains it!

### Regular Index vs Inverted Index
```
Regular Index (like a book's table of contents):
Document -> Words
Doc 1 -> ["cat", "sat", "mat"]
Doc 2 -> ["dog", "ran", "fast"]

Inverted Index (like a book's back index):
Word -> Documents
"cat" -> [Doc 1]
"sat" -> [Doc 1]
"dog" -> [Doc 2]
"fast" -> [Doc 2]
```

### Full-Text Search Process
```
1. User searches: "fast cat"
2. Look up "fast" -> [Doc 2, Doc 5, Doc 8]
3. Look up "cat" -> [Doc 1, Doc 5, Doc 12]
4. Find intersection or union based on query type
   AND: [Doc 5]
   OR: [Doc 1, Doc 2, Doc 5, Doc 8, Doc 12]
5. Rank results by relevance
6. Return top results
```

### Text Processing Pipeline
```
Raw: "The Cats were RUNNING quickly!!"
         |
[Tokenization]: ["The", "Cats", "were", "RUNNING", "quickly"]
         |
[Lowercasing]: ["the", "cats", "were", "running", "quickly"]
         |
[Stop word removal]: ["cats", "running", "quickly"]
         |
[Stemming]: ["cat", "run", "quick"]
         |
Store in inverted index!
```

### Memory Trick
**SEARCH = Stems, Eliminates stop words, And Rapidly Checks the Hash (index)**

### Elasticsearch Architecture
```
[Documents] --> [Analyzer: tokenize, stem, filter]
            --> [Inverted Index: stored across shards]
            --> [Query: search across all shards]
            --> [Merge: combine results from shards]
            --> [Return: ranked results to user]
```

### Today's Quiz
1. Why remove "stop words" like "the", "is", "and"?
2. What is stemming and why is it useful?
3. Design a search system for an email application.

---


## DAY 57: Pub/Sub & Event Streaming (Kafka Deep Dive)

### The Big Idea
Apache Kafka is like a **permanent event newspaper** - events are published, multiple readers can subscribe, and past editions are kept for anyone who wants to read them later!

### Kafka Architecture
```
[Producers] --> [Kafka Cluster] --> [Consumers]
                     |
              [Topic: "orders"]
              [Topic: "payments"]
              [Topic: "user-events"]
```

### Key Concepts

**Topic**: A category/channel (like a newspaper section)
**Partition**: Subdivisions of a topic (for parallelism)
**Producer**: Writes events to topics
**Consumer**: Reads events from topics
**Consumer Group**: Multiple consumers sharing work

```
Topic "orders" with 3 partitions:
Partition 0: [order1, order4, order7, ...]
Partition 1: [order2, order5, order8, ...]
Partition 2: [order3, order6, order9, ...]

Consumer Group A:
  Consumer 1 reads Partition 0
  Consumer 2 reads Partition 1
  Consumer 3 reads Partition 2
  (Each message processed ONCE!)

Consumer Group B:
  Consumer 4 reads ALL partitions
  (Gets ALL messages independently!)
```

### Why Kafka is Special
1. **Persistent**: Messages stored on disk (not deleted after consumption)
2. **Replayable**: Can re-read old messages (rewind!)
3. **Ordered**: Messages within a partition are ordered
4. **Scalable**: Add partitions for more parallelism
5. **Fast**: Can handle millions of messages per second

### Memory Trick
**KAFKA = Keeps All Facts for Anyone (to read anytime)**

### Kafka vs Traditional Message Queue
| Feature | Kafka | RabbitMQ |
|---------|-------|----------|
| Message retention | Days/weeks/forever | Until consumed |
| Replay | Yes | No |
| Ordering | Per partition | Per queue |
| Throughput | Millions/sec | Tens of thousands/sec |
| Best for | Event streaming, data pipelines | Task queues, RPC |

### Real Examples
- **LinkedIn**: 7 trillion messages/day through Kafka
- **Netflix**: Real-time recommendations
- **Uber**: Trip events, driver locations
- **Spotify**: User activity tracking

### Today's Quiz
1. What's the difference between a consumer group and individual consumers?
2. Why does Kafka keep messages after they're consumed?
3. Design an event streaming system for an e-commerce platform.

---

## DAY 58: Graph Databases & Social Networks

### The Big Idea
When your data is all about RELATIONSHIPS (friends, followers, connections), a graph database is like having a map of all connections rather than a spreadsheet!

### Graph Structure
```
(Alice) --[FRIENDS_WITH]--> (Bob)
(Alice) --[LIKES]--> (Photo_123)
(Bob) --[FOLLOWS]--> (Alice)
(Bob) --[WORKS_AT]--> (Google)
```
- **Nodes**: Entities (people, places, things)
- **Edges**: Relationships between nodes
- **Properties**: Data on nodes and edges

### Why Graph Databases?
SQL query for "Friends of friends of Alice":
```sql
SELECT DISTINCT f3.name FROM users f1
JOIN friendships ON f1.id = friendships.user_id
JOIN users f2 ON friendships.friend_id = f2.id
JOIN friendships f2_friends ON f2.id = f2_friends.user_id
JOIN users f3 ON f2_friends.friend_id = f3.id
WHERE f1.name = 'Alice'
-- COMPLEX AND SLOW!
```

Graph query (Cypher):
```cypher
MATCH (alice:User {name:'Alice'})-[:FRIEND]->()-[:FRIEND]->(fof)
RETURN fof.name
-- Simple and FAST!
```

### Use Cases
- **Social Networks**: Friend recommendations ("People you may know")
- **Fraud Detection**: Finding suspicious transaction patterns
- **Recommendation Engines**: "People who bought X also bought Y"
- **Knowledge Graphs**: Google's search understanding
- **Network/IT**: Mapping infrastructure dependencies

### Memory Trick
**GRAPH = Greatly Reveals All Paths & Hidden connections**

### Popular Graph Databases
- **Neo4j**: Most popular, uses Cypher query language
- **Amazon Neptune**: Managed cloud graph DB
- **JanusGraph**: Distributed, open source
- **Dgraph**: Distributed, uses GraphQL

### Today's Quiz
1. When is a graph database better than SQL?
2. How would you find "mutual friends" in a graph?
3. Design a "People You May Know" feature using a graph.

---

## DAY 59: Content Moderation Systems

### The Big Idea
How do platforms like YouTube, Instagram, and Twitter detect and remove harmful content? It's a mix of AI (automated detection) and human review!

### Architecture
```
[Content Upload] --> [Pre-filter: check size, format]
                      |
              [AI Detection Layer]
              |          |          |
         [Text AI]  [Image AI]  [Video AI]
              |          |          |
         [Score: 0-1 probability of violation]
                      |
           [Decision Engine]
           /      |       \
    [Auto-Allow] [Queue for Review] [Auto-Block]
     (score <0.3)  (0.3-0.8)        (score >0.8)
                    |
            [Human Moderator]
             /           \
       [Approve]      [Remove + Strike]
```

### Types of Detection
1. **Text**: Hate speech, harassment, spam (NLP models)
2. **Image**: Nudity, violence, copyrighted material (Computer Vision)
3. **Video**: Harmful content frame-by-frame (expensive!)
4. **Audio**: Hate speech in podcasts/livestreams (Speech-to-text + NLP)

### Key Design Decisions
- **Precision vs Recall**: Block too much (false positives) or miss harmful content (false negatives)?
- **Speed vs Accuracy**: Block immediately with simple model or wait for complex analysis?
- **Appeals**: Users can challenge decisions

### Memory Trick
**MODERATE = Machines Observe, Detect Extremes, Review Ambiguous Things, Escalate**

### Scale Challenge
- YouTube: 500 hours of video uploaded per MINUTE
- Can't have humans watch everything!
- AI handles 99%, humans handle the edge cases

### Today's Quiz
1. Why can't you rely only on AI for content moderation?
2. What's the trade-off between precision and recall?
3. Design a content moderation system for a social media platform.

---

## DAY 60: System Design Patterns Summary

### The Big Idea
Let's consolidate all the patterns you've learned into a quick-reference guide!

### Pattern Cheat Sheet

| Problem | Pattern | Example |
|---------|---------|---------|
| Too many users | Horizontal Scaling + Load Balancer | Netflix |
| Slow reads | Caching (Redis) + CDN | Instagram |
| Data too big for one DB | Sharding | Discord |
| Service failures | Circuit Breaker | Netflix |
| Multi-step transactions | Saga Pattern | E-commerce orders |
| Finding nearest X | Geospatial Index | Uber |
| Preventing duplicates | Idempotency Keys | Payment systems |
| Decoupling services | Message Queue / Event Bus | Any microservices |
| Real-time updates | WebSockets / SSE | Chat apps |
| Search | Inverted Index / Elasticsearch | Google, GitHub |
| Rate abuse | Rate Limiting | API gateways |
| High availability | Replication + Failover | Banking |
| Unique IDs | Snowflake | Twitter |
| Smart data distribution | Consistent Hashing | Cassandra |
| Read/Write optimization | CQRS | News feeds |

### Phase 3 Checklist
- [ ] Unique ID Generation
- [ ] Bloom Filters
- [ ] Geospatial Indexing
- [ ] Counters at Scale
- [ ] Notification Systems
- [ ] Distributed Locking
- [ ] Data Rebalancing
- [ ] Gossip Protocol
- [ ] Service Discovery
- [ ] Data Serialization
- [ ] Heartbeat & Failure Detection
- [ ] Conflict Resolution
- [ ] Back-of-envelope Estimation
- [ ] Connection Pooling
- [ ] CQRS
- [ ] Full-Text Search
- [ ] Kafka & Event Streaming
- [ ] Graph Databases
- [ ] Content Moderation
- [ ] Patterns Summary

---

# MINI PROJECT: Design a Ride-Sharing System
Design Uber/Lyft with:
- Riders request rides with pickup and destination
- System matches rider with nearest available driver
- Real-time location tracking during ride
- Fare calculation and payment
- Rating system
- Surge pricing during peak hours

Use concepts from ALL three phases!

---


---

# PHASE 4: REAL SYSTEM DESIGNS (Days 61-85)
## Design Famous Systems Step by Step

---

## DAY 61-63: Design Twitter/X

### Requirements
- Post tweets (280 characters + images/videos)
- Follow/Unfollow users
- News Feed (timeline of people you follow)
- Search tweets
- Trending topics
- Like, Retweet, Reply

### Scale
- 500M tweets/day, 300M active users
- Read-heavy (100:1 read/write ratio)
- Celebrity problem: User with 50M followers posts, 50M feeds update!

### High-Level Architecture
```
[Mobile/Web Client]
        |
[API Gateway + Load Balancer]
        |
[Tweet Service]  [Feed Service]  [User Service]  [Search Service]
        |              |               |               |
[Tweet DB]     [Feed Cache]    [User DB]     [Elasticsearch]
(Sharded)       (Redis)        (Sharded)     (Inverted Index)
        |
[Object Storage: images/videos]
        |
[CDN: serve media]
```

### Feed Generation: Two Approaches

**1. Pull Model (Fan-out on Read)**
```
When user opens timeline:
1. Get list of people they follow
2. Get recent tweets from each person
3. Merge and sort by time
4. Return top N tweets
```
- Slow for users following many people
- Good for celebrities (no fan-out on write)

**2. Push Model (Fan-out on Write)**
```
When user tweets:
1. Get all followers (50M for celebrities!)
2. Push tweet into each follower's feed cache
3. When follower opens app, feed is ready!
```
- Fast reads but expensive writes
- Bad for celebrities (50M cache updates per tweet!)

**3. Hybrid (Twitter's actual approach)**
- Regular users: Push model (pre-compute feeds)
- Celebrities (>10K followers): Pull model (fetch on demand)
- Merge both at read time!

### Database Schema
```
Users: {user_id, name, email, bio, follower_count}
Tweets: {tweet_id, user_id, content, media_urls, created_at, like_count}
Follows: {follower_id, following_id, created_at}
Likes: {user_id, tweet_id, created_at}
```

### Key Decisions
- Tweet ID: Snowflake (sortable by time)
- Feed storage: Redis sorted sets (sorted by timestamp)
- Media: S3 + CDN
- Search: Elasticsearch with inverted index
- Trending: Stream processing on tweet text (count hashtags in sliding window)

### Memory Trick for Twitter Design
**TWITTER = Tweets Written In Timeline, Topics Everywhere Ranked**

---

## DAY 64-66: Design Instagram

### Requirements
- Upload photos/videos with captions
- Follow users
- News Feed with photos from followed users
- Like and comment on posts
- Stories (24-hour disappearing content)
- Explore page (recommendations)
- Direct messaging

### Scale
- 2 billion monthly active users
- 100M photos uploaded daily
- Average photo: 1MB, stored in multiple sizes

### Architecture
```
[Client] --> [API Gateway]
                 |
    +------------+------------+------------+
    |            |            |            |
[Upload]    [Feed]      [Search]     [Stories]
[Service]   [Service]   [Service]    [Service]
    |            |            |            |
[S3 + CDN]  [Redis]    [Elastic]    [Redis TTL]
    |
[Image Processing Pipeline]
- Resize to: thumbnail (150px), medium (600px), full (1080px)
- Strip metadata
- Apply filters
- Store all versions
```

### Photo Upload Flow
```
1. Client uploads photo to Upload Service
2. Upload Service stores in temporary storage
3. Async job: Resize, filter, generate thumbnails
4. Store all versions in S3
5. Update database with photo URLs
6. Push notification to followers' feed cache
7. CDN serves photos to viewers
```

### Feed Generation
- Same hybrid approach as Twitter
- Pre-compute feed for regular users
- On-demand for celebrity accounts
- Sort by: engagement prediction (not just chronological)

### Stories Architecture
```
Stories expire after 24 hours:
- Store with TTL (Time To Live) in Redis
- When TTL expires, automatically deleted
- Stories are viewed sequentially (different from feed)
- Viewer list stored per story
```

### Storage Estimation
```
100M photos/day × 1MB × 4 sizes = 400 TB/day
Per year: 400 TB × 365 = 146 PB
With 3x replication: ~438 PB
CDN handles most reads (reduces origin load by 90%)
```

### Key Decisions
- ID: Snowflake (sortable, includes shard info)
- Sharding: By user_id (all of a user's photos on same shard)
- Cache: Redis for feeds and active stories
- Object Storage: S3 for photos/videos
- CDN: CloudFront for global distribution
- ML: Recommendation model for Explore page

---

## DAY 67-69: Design YouTube/Netflix Video Streaming

### Requirements
- Upload videos (YouTube)
- Stream videos in different qualities
- Recommendations
- Comments, likes, subscriptions
- Live streaming
- Search

### Scale (YouTube)
- 500 hours of video uploaded per minute
- 1 billion hours watched per day
- Available in 100+ countries

### Video Upload & Processing Pipeline
```
[Upload] --> [Chunk video] --> [Transcode Queue]
                                     |
              +----------------------+----------------------+
              |                      |                      |
      [Transcode to 360p]   [Transcode to 720p]   [Transcode to 1080p]
      [Transcode to 1440p]  [Transcode to 4K]
              |                      |                      |
      [Generate thumbnails]  [Extract subtitles]   [Content check (AI)]
              |
      [Store all versions in Object Storage]
              |
      [Update metadata DB]
              |
      [Distribute to CDN edges worldwide]
```

### Adaptive Bitrate Streaming
```
User watching on mobile with spotty internet:
- Start with 720p
- Network drops: Seamlessly switch to 480p
- Network recovers: Switch back to 720p
- User never notices!

How: Video split into 2-10 second chunks
Each chunk available in ALL qualities
Player chooses quality per chunk based on bandwidth
```

### Architecture
```
[Client] --> [CDN Edge: serve cached video chunks]
                |
         [Origin: full video library on Object Storage]
                |
         [Metadata Service: video info, comments, likes]
                |
         [Recommendation Service: ML-based suggestions]
                |
         [Search Service: Elasticsearch]
                |
         [Analytics: view counts, watch time]
```

### Netflix-Specific: Open Connect
- Netflix builds their own CDN appliances
- Places them INSIDE ISP networks
- 90% of traffic served from these local boxes
- Result: No buffering, fast starts!

### Storage Estimation (YouTube)
```
500 hours/min × 60 min × 24 hours = 720,000 hours/day
Average video length: 5 min, average size per quality: 50MB
5 quality levels: 50MB × 5 = 250MB per video
720,000 hours = 8,640,000 videos/day
Storage per day: 8.64M × 250MB = ~2.16 PB/day!
```

### Key Decisions
- Upload: Direct to Object Storage (not through app server)
- Processing: Distributed workers, message queue (Kafka)
- Serving: CDN for all video content
- Database: Metadata in Cassandra (high write throughput)
- Recommendations: Collaborative filtering + deep learning
- Thumbnails: Pre-generated, A/B tested

---


## DAY 70-72: Design WhatsApp/Messaging System

### Requirements
- One-on-one chat
- Group chat (up to 256 members)
- Message delivery status (sent, delivered, read)
- Online/offline status
- Media sharing (images, videos, documents)
- End-to-end encryption
- Message persistence

### Scale
- 2 billion users
- 100 billion messages per day
- Real-time delivery (< 100ms latency)

### Architecture
```
[Phone A] --WebSocket--> [Chat Server 1]
                              |
                    [Message Queue (Kafka)]
                              |
                    [Routing Service: Find recipient's chat server]
                              |
[Phone B] <--WebSocket-- [Chat Server 2]
```

### Message Flow (1-on-1)
```
1. Alice sends "Hi!" to Bob
2. Alice's phone --> WebSocket --> Chat Server A
3. Chat Server A --> Store message in DB (status: SENT)
4. Chat Server A --> Route to Bob's Chat Server
5. Chat Server B --> Push to Bob's phone via WebSocket
6. Bob's phone receives --> Server marks: DELIVERED
7. Bob opens chat --> Server marks: READ
8. Alice sees double blue check!
```

### Group Chat
```
Alice sends to Group "Family" (4 members):
1. Message goes to Chat Server
2. Server looks up group members: [Alice, Bob, Charlie, Diana]
3. Server sends to each member's chat server (fan-out)
4. Each delivery tracked separately
```

### Offline Handling
```
Bob is offline:
1. Message stored in "pending messages" queue for Bob
2. When Bob comes online (WebSocket reconnects):
   - Server sends all pending messages
   - Marks as DELIVERED
```

### End-to-End Encryption
```
- Only sender and receiver can read messages
- Server stores ENCRYPTED messages (can't read them!)
- Signal Protocol: Key exchange on first connection
- Each message encrypted with session key
- Even WhatsApp servers can't decrypt!
```

### Database Choices
- Messages: Cassandra (high write throughput, time-series like)
- User profiles: PostgreSQL
- Online status: Redis (fast, in-memory, TTL)
- Media: S3 + CDN
- Message queue: Kafka (reliable, ordered)

### Key Decisions
- WebSocket for real-time bidirectional communication
- Shard by user_id (all conversations for a user on same shard)
- Fan-out at write time for groups (max 256, manageable)
- Message retention: Store encrypted messages for delivery, then only on devices

---

## DAY 73-75: Design Uber/Ride-Sharing

### Requirements
- Rider requests ride (pickup location, destination)
- Match with nearest available driver
- Real-time driver location tracking
- ETA calculation
- Fare estimation and payment
- Rating system
- Surge pricing

### Scale
- 100 million riders, 5 million drivers
- 20 million rides per day
- Location update every 4 seconds from active drivers

### Architecture
```
[Rider App] --> [API Gateway] --> [Ride Matching Service]
[Driver App]         |            [Location Service]
                     |            [Payment Service]
                     |            [Pricing Service]
                     |            [Trip Service]
                     |            [Notification Service]
```

### The Matching Problem
```
Rider requests ride at point X:
1. Location Service: Find all available drivers within 5km of X
2. Filter: Only drivers going in right direction
3. Calculate ETA for each nearby driver
4. Pick best match (closest ETA + rating)
5. Notify driver: "New ride request!"
6. Driver has 15 seconds to accept
7. If declined/timeout: Ask next driver
```

### Location Tracking (Core Challenge)
```
5M active drivers × 1 update every 4 seconds = 1.25M location updates/second!

Solution:
- Use Geohash for spatial indexing
- Store current locations in Redis (fast reads/writes)
- When driver moves: Update geohash cell
- When rider searches: Query nearby geohash cells

[Driver Location Update Flow]
Driver GPS --> API --> Redis: SET driver:123 {lat, lng, geohash, status}
                   --> Kafka: Stream for analytics/ETA
```

### Geofencing & Cells
```
City divided into hexagonal cells:
Each cell tracked separately
Supply (drivers in cell) vs Demand (ride requests in cell)
If demand > supply: Surge pricing in that cell!
```

### ETA Calculation
- Not just straight-line distance!
- Uses road network graph
- Traffic data (real-time from driver speeds)
- Historical patterns (rush hour, events)
- Dijkstra's algorithm on road graph

### Fare Calculation
```
fare = base_fare
     + (per_minute × trip_duration)
     + (per_mile × trip_distance)
     + surge_multiplier
     + tolls
     + service_fee
     - promotions/discounts
```

### Key Decisions
- Location: Redis with geohash for real-time
- Matching: Custom algorithm (not simple "nearest")
- Communication: WebSocket for real-time tracking
- Payment: Saga pattern (ride -> calculate fare -> charge -> pay driver)
- Surge: Stream processing on ride requests per cell

---

## DAY 76-78: Design Google Search

### Requirements
- Crawl the web (billions of pages)
- Index all content
- Rank results by relevance
- Return results in < 500ms
- Handle 100K queries per second
- Autocomplete suggestions

### Architecture
```
[Web Pages] --> [Crawler] --> [Parser] --> [Indexer] --> [Index Storage]
                                                              |
[User Query] --> [Query Service] --> [Ranking] --> [Results]
```

### Step 1: Web Crawling
```
1. Start with seed URLs (known websites)
2. Download page, extract all links
3. Add new links to queue
4. Respect robots.txt (what NOT to crawl)
5. Politeness: Don't overwhelm one site (rate limit per domain)
6. Freshness: Re-crawl important pages more often

Scale: Billions of pages, trillions of links!
Distributed across thousands of crawler machines.
```

### Step 2: Indexing
```
For each page:
1. Parse HTML: extract text, links, metadata
2. Tokenize text: split into words
3. Remove stop words, stem words
4. Build inverted index:
   "computer" -> [page_1 (title, pos:5), page_2 (body, pos:120), ...]
5. Store page quality signals (PageRank, freshness, etc.)
```

### Step 3: Ranking (PageRank + Hundreds of Signals)
```
PageRank: Pages linked by important pages are more important!
Like academic citations: Paper cited by Nature > paper cited by no one.

More signals:
- Content relevance (TF-IDF)
- Freshness (recent = better for news)
- User location (local results)
- Page load speed
- Mobile-friendly
- HTTPS (secure)
- User engagement (click-through rate)
```

### Step 4: Query Processing
```
User types: "best pizza near me"
1. Query understanding: Intent = local restaurant search
2. Expansion: Add synonyms, correct spelling
3. Retrieve: Get candidate pages from inverted index
4. Rank: Apply ranking algorithm
5. Personalize: User's location, search history
6. Serve: Return top 10 with snippets
7. Total time: < 200ms!
```

### Autocomplete
```
User types: "how to ma..."
System suggests: "how to make pasta"
                "how to make money online"
                "how to make friends"

Implementation:
- Trie data structure (prefix tree)
- Weighted by search frequency
- Updated in real-time from trending queries
- Cached heavily (most queries are common)
```

### Key Decisions
- Crawl storage: Distributed file system (Bigtable)
- Index: Sharded across thousands of servers
- Serving: Multiple levels of cache
- Ranking: ML model with 200+ features
- Freshness: Different crawl rates for different page types

---

## DAY 79-81: Design Amazon E-Commerce

### Requirements
- Product catalog (100M+ products)
- Search and browse products
- Shopping cart
- Order placement and payment
- Inventory management
- Reviews and ratings
- Recommendations
- Order tracking

### Architecture (Microservices)
```
[Web/Mobile] --> [API Gateway]
                      |
    +--------+--------+--------+--------+--------+
    |        |        |        |        |        |
[Product] [Search] [Cart]  [Order] [Payment] [Inventory]
[Service] [Service][Service][Service][Service] [Service]
    |        |        |        |        |        |
[PostgreSQL][Elastic][Redis] [MySQL] [Payment] [DynamoDB]
             search                   Provider
```

### Product Catalog
```
- 100M+ products
- Each product: name, description, images, price, categories, attributes
- Read-heavy (1000:1 read/write)
- Search by: name, category, brand, price range, ratings
- Different types: Books, Electronics, Clothing (different attributes!)

Design:
- PostgreSQL for structured product data
- Elasticsearch for full-text search + filters
- Redis cache for popular products
- CDN for product images
```

### Shopping Cart
```
Requirements:
- Persist across sessions (user leaves and comes back)
- Work across devices (add on phone, checkout on laptop)
- Handle concurrent updates

Design:
- Logged-in users: Store in database (DynamoDB - fast key-value)
- Guest users: Store in cookies/localStorage + sync on login
- Merge: When guest creates account, merge cart
```

### Order Flow (Saga Pattern!)
```
1. Validate cart items (still in stock?) ✓
2. Reserve inventory (hold for 10 minutes) ✓
3. Process payment (charge card) ✓
4. Confirm order (create order record) ✓
5. Notify seller (prepare for shipping) ✓
6. Send confirmation email ✓

If Step 3 (payment) fails:
- Compensate Step 2: Release inventory reservation
- Notify user: "Payment failed"
```

### Inventory Management (Critical!)
```
Challenge: 1000 people trying to buy the last item!

Solution: Pessimistic Locking
1. User clicks "Buy" -> Lock that item's inventory row
2. Check: quantity > 0?
   Yes: Decrement, proceed to payment
   No: "Sorry, sold out!"
3. Release lock

OR: Optimistic with versioning
1. Read: {item: "Widget", qty: 1, version: 5}
2. Update: SET qty=0 WHERE version=5
   If success: Proceed!
   If fail (version changed): Someone else got it, retry/show "sold out"
```

### Recommendations
```
"Customers who bought X also bought Y"
- Collaborative filtering: Find similar users, suggest their purchases
- Content-based: Find similar products by features
- Real-time: "Based on your browsing history..."
- Batch: Pre-compute popular recommendations overnight
```

### Key Decisions
- Cart: DynamoDB (fast, scalable key-value)
- Products: PostgreSQL + Elasticsearch + Redis cache
- Orders: MySQL with strong ACID guarantees
- Inventory: DynamoDB with conditional writes
- Recommendations: Pre-computed + real-time ML
- Images: S3 + CDN
- Events: Kafka for order events, analytics

---


## DAY 82-83: Design a Payment System (Stripe/PayPal)

### Requirements
- Accept payments (credit card, bank transfer)
- Process refunds
- Handle multiple currencies
- Prevent double charging
- PCI compliance (security)
- Webhook notifications to merchants
- Ledger/accounting records

### Architecture
```
[Merchant's App] --> [Payment Gateway API]
                           |
                    [Payment Orchestrator]
                    /         |         \
        [Fraud Check]  [Currency Conv]  [Routing]
                           |
                    [Payment Processor]
                    (Visa/Mastercard/Bank)
                           |
                    [Ledger Service]
                    (Double-entry bookkeeping)
```

### Payment Flow
```
1. Merchant sends: {amount: $50, card: "4242...", idempotency_key: "abc"}
2. Fraud check: Is this suspicious? (ML model)
3. Tokenize card: Store token, not actual card number (PCI compliance)
4. Route to correct processor (Visa, Mastercard, etc.)
5. Processor authorizes (holds money on card)
6. Capture payment (actually moves money)
7. Record in ledger
8. Send webhook to merchant: "Payment successful!"
```

### Critical: Idempotency
```
Why: Network failures can cause retries
- User clicks Pay, network drops, app retries
- WITHOUT idempotency: User charged twice!
- WITH idempotency: Second request returns same result as first

Implementation:
- Client sends unique idempotency_key with each request
- Server stores: {key: "abc", result: "success", amount: $50}
- On retry: Server recognizes key, returns stored result
```

### Double-Entry Ledger
```
Every transaction has TWO entries (always balanced):

Payment of $50 from User to Merchant:
| Account    | Debit  | Credit |
|-----------|--------|--------|
| User      | $50    |        |
| Merchant  |        | $50    |

Debit total ALWAYS equals Credit total!
This is how banks prevent "money disappearing"
```

### Handling Failures
```
Payment authorized but capture fails:
- Retry capture with exponential backoff
- After X retries: void the authorization
- Alert operations team

Refund fails:
- Queue for retry
- Track in separate refund state machine
- States: PENDING -> PROCESSING -> COMPLETED/FAILED
```

### Key Decisions
- Database: PostgreSQL (ACID for financial data)
- Idempotency: Required on ALL write operations
- Events: Kafka for async processing and auditing
- Encryption: All card data encrypted at rest and in transit
- Reconciliation: Daily batch job comparing our records vs bank records

---

## DAY 84-85: Design a Notification/Alert System (Like PagerDuty)

### Requirements
- Multi-channel: Email, SMS, Push, Slack, Phone call
- Alert routing: Send to the right person based on rules
- Escalation: If not acknowledged in X minutes, alert next person
- Scheduling: Who's on-call right now?
- Aggregation: Don't send 100 alerts for same issue
- Templates: Customizable alert messages

### Architecture
```
[Alert Source] --> [Alert Ingestion API]
(Monitoring tools)        |
                   [Alert Processing Engine]
                          |
                   [Deduplication: Is this a repeat?]
                          |
                   [Routing: Who gets this?]
                          |
                   [Escalation Engine]
                   /       |       \
           [Email]    [SMS]     [Phone Call]
           [Push]     [Slack]   [Webhook]
```

### Escalation Flow
```
Alert: "Server CPU at 99%!"

Minute 0: Send to on-call engineer (Level 1)
Minute 5: Not acknowledged -> Escalate to backup (Level 2)
Minute 10: Not acknowledged -> Escalate to team lead (Level 3)
Minute 15: Not acknowledged -> Page entire team + manager
Minute 30: Still unresolved -> Escalate to VP of Engineering
```

### On-Call Schedule
```
Weekly rotation:
Week 1: Alice (primary), Bob (secondary)
Week 2: Bob (primary), Charlie (secondary)
Week 3: Charlie (primary), Alice (secondary)

Override: If Alice is on vacation, route to secondary
```

### Alert Aggregation (Critical!)
```
Problem: Server has 500 errors per second
Without aggregation: 500 alerts per second (unusable!)
With aggregation:
- First alert: Send immediately
- Next 5 minutes: Suppress, count occurrences
- After 5 minutes: "500 errors occurred in last 5 minutes" (ONE alert)
```

### State Machine for Alert Lifecycle
```
[TRIGGERED] --> [ACKNOWLEDGED] --> [RESOLVED]
     |               |
     |          [ESCALATED] (if timeout)
     |
[AUTO-RESOLVED] (if condition clears)
```

### Key Decisions
- Queue: Kafka for ingestion (high throughput, reliable)
- Timer: Scheduled jobs for escalation (Redis sorted sets)
- State: PostgreSQL for alert state and history
- Dedup: Redis with TTL (key = alert fingerprint)
- Delivery: Separate workers per channel (email, SMS, etc.)

---


---

# PHASE 5: ADVANCED & INTERVIEW PREP (Days 86-100)
## Master Level - Putting It All Together

---

## DAY 86: Designing for Failure

### The Big Idea
In distributed systems, failure is not IF but WHEN. Great system designers don't try to prevent ALL failures - they design systems that SURVIVE failures gracefully!

### Types of Failures
1. **Hardware**: Disk dies, server crashes, network card fails
2. **Software**: Bug causes crash, memory leak, deadlock
3. **Network**: Packet loss, partition, latency spike
4. **Human**: Wrong config deployed, wrong server shut down
5. **Dependencies**: Third-party API down, cloud region outage

### Failure Design Patterns

**1. Graceful Degradation**
- When part of system fails, reduce features but stay alive
- Netflix: If recommendation service dies, show popular titles instead
- Amazon: If review service dies, show product without reviews

**2. Bulkhead Pattern**
- Isolate components so one failure doesn't sink everything
- Like compartments in a ship: flood one, others stay dry
```
[Thread Pool: Payment] (10 threads)
[Thread Pool: Search] (20 threads)
[Thread Pool: Recommendations] (5 threads)
If search takes all threads, payment still works!
```

**3. Chaos Engineering**
- Netflix's Chaos Monkey: Randomly kills servers in production!
- Purpose: Find weaknesses before real failures do
- If your system survives random server deaths, it's resilient!

**4. Redundancy at Every Layer**
```
[Multiple Load Balancers]
        |
[Multiple App Servers]
        |
[Multiple Databases (replicas)]
        |
[Multiple Data Centers]
No single point of failure!
```

### Memory Trick
**FAILURE = Find And Investigate, Limit the blast radius, Use redundancy, Recover Easily**

### Post-Mortem Culture
After every failure:
1. What happened? (Timeline)
2. What was the impact? (Users affected)
3. Why did it happen? (Root cause - ask "Why?" 5 times)
4. How do we prevent it? (Action items)
5. Blameless! (Focus on systems, not people)

### Today's Quiz
1. What is the Bulkhead pattern?
2. Why does Netflix randomly kill its own servers?
3. Design a system that survives an entire data center going offline.

---

## DAY 87: Multi-Region & Global Distribution

### The Big Idea
Users are everywhere. Your servers should be too! Multi-region design puts your system in data centers around the world.

### Why Multi-Region?
1. **Latency**: Users connect to nearest region (100ms vs 500ms)
2. **Availability**: If one region dies, others handle traffic
3. **Compliance**: Some data must stay in certain countries (GDPR)
4. **Disaster Recovery**: Natural disasters don't affect all regions

### Architecture
```
[Users in Asia] --> [Asia Region]
                    - App Servers
                    - Database Replica
                    - Cache

[Users in US] --> [US Region (Primary)]
                  - App Servers
                  - Database Primary
                  - Cache

[Users in EU] --> [EU Region]
                  - App Servers
                  - Database Replica
                  - Cache

All regions sync via replication!
```

### Routing Strategies
1. **GeoDNS**: DNS resolves to nearest region based on user's IP
2. **Anycast**: Same IP, network routes to nearest server
3. **Global Load Balancer**: Smart routing based on health + latency

### The Hard Part: Data Consistency
- Data written in US must be readable in Asia
- Replication lag: 100-300ms between regions
- Options:
  - Strong consistency: All writes go to one region (slow for far users)
  - Eventual consistency: Write locally, sync later (fast but stale)
  - Conflict resolution: Write anywhere, resolve conflicts

### Active-Active vs Active-Passive

**Active-Passive:**
- One region handles all writes
- Others are read-only replicas
- If primary dies: Promote a passive region (minutes of downtime)

**Active-Active:**
- All regions handle reads AND writes
- More complex (conflict resolution needed)
- Zero downtime during regional failure
- Used by: Google, Facebook, Amazon

### Memory Trick
**GLOBAL = Get Latency Optimal By Adding Locations**

### Today's Quiz
1. What's the trade-off between active-active and active-passive?
2. How does GDPR affect multi-region design?
3. If US-East goes down, how does traffic switch to US-West?

---

## DAY 88: Security in System Design

### The Big Idea
Security is not a feature you add later - it must be designed in from the start! Think of it as building a house with locks, alarms, and a safe rather than adding them after moving in.

### Security Layers (Defense in Depth)
```
[Users/Attackers]
      |
[Layer 1: DDoS Protection (CloudFlare)]
      |
[Layer 2: Firewall (WAF - Web Application Firewall)]
      |
[Layer 3: API Gateway (Auth, Rate Limiting)]
      |
[Layer 4: Application (Input validation, CSRF protection)]
      |
[Layer 5: Database (Encryption, Access control)]
      |
[Layer 6: Network (VPC, Private subnets)]
```

### Common Attacks & Defenses

**1. SQL Injection**
```
Attack: Username = "admin'; DROP TABLE users; --"
Defense: Use parameterized queries, NEVER concatenate SQL!
```

**2. DDoS (Distributed Denial of Service)**
```
Attack: Millions of fake requests overwhelm server
Defense: CDN, rate limiting, DDoS protection services
```

**3. XSS (Cross-Site Scripting)**
```
Attack: Inject malicious JavaScript into web page
Defense: Sanitize all user input, Content Security Policy
```

**4. Man-in-the-Middle**
```
Attack: Intercepting communication between client and server
Defense: HTTPS everywhere, certificate pinning
```

### Encryption
- **At Rest**: Data encrypted in database/storage (AES-256)
- **In Transit**: Data encrypted during transmission (TLS/HTTPS)
- **End-to-End**: Only sender and receiver can read (Signal protocol)

### Principle of Least Privilege
- Every component gets MINIMUM permissions needed
- Database user for app: Only SELECT, INSERT, UPDATE (not DROP!)
- Microservice: Only access the APIs it needs
- Like giving hotel staff a master key vs room-specific keys

### Memory Trick
**SECURE = Sanitize inputs, Encrypt everything, Control access, Use HTTPS, Rate limit, Educate users**

### Today's Quiz
1. What is "defense in depth"?
2. Why should you never store passwords in plain text?
3. Design the security architecture for a banking application.

---

## DAY 89: Performance Optimization

### The Big Idea
Making your system faster is about finding and fixing BOTTLENECKS. Like a chain - it's only as strong as its weakest link!

### Where Time Goes (Response Time Breakdown)
```
Total: 500ms
  - DNS lookup: 20ms
  - TCP connection: 50ms
  - TLS handshake: 100ms
  - Server processing: 200ms
  - Database query: 100ms
  - Network transfer: 30ms

Biggest bottleneck: Server processing (200ms)!
Focus optimization there.
```

### Optimization Techniques (by Layer)

**Frontend:**
- Minify CSS/JS (smaller files)
- Compress images (WebP format)
- Lazy loading (load images when visible)
- Browser caching (static assets)

**Network:**
- CDN for static content
- HTTP/2 (multiplexing)
- Compression (gzip/brotli)
- Connection pooling

**Application:**
- Caching (Redis)
- Async processing (queues)
- Efficient algorithms
- Connection pooling

**Database:**
- Indexing (most impactful!)
- Query optimization
- Read replicas
- Denormalization
- Connection pooling

### The 80/20 Rule
- 80% of time is spent on 20% of operations
- Find those 20% and optimize them first!
- Don't optimize what doesn't matter

### Profiling & Benchmarking
- **APM tools**: New Relic, Datadog (find slow endpoints)
- **Database**: EXPLAIN ANALYZE (see query plans)
- **Load testing**: JMeter, k6 (test under load)
- **Metrics**: P50, P90, P99 latency (percentiles matter!)

### Memory Trick
**PERFORMANCE = Profile, Eliminate bottlenecks, Reduce latency, Find the 80/20, Optimize the hot path, Replace slow queries, Measure Again, Not premature, Cache Everything, Eliminate waste**

### Today's Quiz
1. What's the difference between P50 and P99 latency?
2. Why is premature optimization dangerous?
3. You have a 2-second page load. How would you identify what to optimize?

---


## DAY 90: Capacity Planning

### The Big Idea
Capacity planning is figuring out HOW MUCH of everything you need. How many servers? How much storage? How much bandwidth? Plan ahead so you don't run out!

### The Planning Process
1. **Estimate traffic**: How many users? How many requests/second?
2. **Estimate storage**: How much data? How fast does it grow?
3. **Estimate bandwidth**: How much data transferred?
4. **Estimate compute**: How many servers needed?
5. **Plan for growth**: 2x or 10x in next year?

### Example: Plan Capacity for Twitter

**Traffic Estimation:**
```
300M daily active users (DAU)
Average user: 5 timeline views, 2 tweets, 20 likes per day
Read requests: 300M × 5 = 1.5B/day = 17,360/second
Write requests: 300M × 2 = 600M/day = 6,944/second
Total QPS: ~25,000/second (peak might be 3x = 75,000/sec)
```

**Storage Estimation:**
```
500M tweets/day × 300 bytes/tweet = 150 GB/day text
50M media tweets/day × 1MB average = 50 TB/day media
Per year: (150 GB + 50 TB) × 365 = ~18 PB/year
With replication (3x): ~54 PB/year
```

**Bandwidth:**
```
Read bandwidth: 1.5B views × average 500KB (text + images) = 750 TB/day
= 8.7 GB/second outbound
Write bandwidth: 150 GB + 50 TB = ~50 TB/day inbound
= 580 MB/second inbound
```

**Server Estimation:**
```
If one server handles 10,000 QPS:
Need: 75,000 / 10,000 = 8 app servers (minimum)
With headroom (50% utilization): 16 servers
Add redundancy (N+2): 18 servers minimum
```

### Memory Trick
**CAPACITY = Calculate And Plan All Components Including Tomorrow's Yield**

### Always Add Buffer
- Plan for 3-5x your estimated peak
- Growth is usually faster than you think
- Running out of capacity = downtime = lost revenue

### Today's Quiz
1. Estimate storage for YouTube (500 hours video/minute)
2. If each server handles 5000 QPS, how many servers for 100K QPS with redundancy?
3. What happens if you underestimate capacity?

---

## DAY 91: System Design Interview Framework

### The Big Idea
System design interviews are as much about your PROCESS as your answer. Interviewers want to see HOW you think, not just the final diagram!

### The 45-Minute Framework

**Step 1: Requirements & Scope (5 min)**
```
Ask:
- What features? (Core features only, not all)
- How many users? (Scale determines architecture)
- Read-heavy or write-heavy?
- Latency requirements?
- Data retention?
- Global or single region?

Example: "Design Instagram"
You ask: "Should I focus on feed, upload, or stories?"
Interviewer: "Focus on photo upload and feed generation"
```

**Step 2: Capacity Estimation (5 min)**
```
Quick math:
- QPS (queries per second)
- Storage needed
- Bandwidth
- Number of servers

Show your math! Even if off by 2x, process matters.
```

**Step 3: High-Level Design (10 min)**
```
Draw the big picture:
- Main components (boxes)
- Data flow (arrows)
- Client -> Load Balancer -> Services -> Databases
- Keep it simple! 5-7 components max.
```

**Step 4: Detailed Design (15 min)**
```
Deep dive into 2-3 key components:
- Database schema
- API design
- Key algorithms
- Data flow for critical paths
- This is where you show expertise!
```

**Step 5: Scalability & Trade-offs (10 min)**
```
Discuss:
- How to handle 10x, 100x scale?
- What are the bottlenecks?
- Trade-offs you made and why
- Monitoring and alerting
- Failure scenarios and handling
```

### Golden Rules
1. **NEVER start coding** - this is architecture, not implementation
2. **Always ask clarifying questions** - shows maturity
3. **Think out loud** - interviewer can't read your mind
4. **Discuss trade-offs** - there's no perfect answer
5. **Don't try to cover everything** - depth > breadth

### Memory Trick
**HIRED = Highlight requirements, Illustrate high-level, Refine details, Evaluate scale, Discuss trade-offs**

### Common Mistakes
- Jumping into details too quickly
- Not asking questions
- Designing for too many features
- Ignoring scalability
- Being silent (think out loud!)
- Over-engineering a simple problem

---

## DAY 92: Common Interview Questions & Approaches

### Top 20 System Design Questions

**1. Design URL Shortener (bit.ly)**
Key: Hash function, Base62 encoding, read-heavy caching

**2. Design Twitter/Social Feed**
Key: Fan-out strategies, caching, timeline generation

**3. Design Instagram**
Key: Media storage, CDN, feed ranking

**4. Design WhatsApp/Chat System**
Key: WebSockets, message delivery guarantees, E2E encryption

**5. Design YouTube/Netflix**
Key: Video transcoding pipeline, adaptive streaming, CDN

**6. Design Uber/Lyft**
Key: Geospatial indexing, real-time matching, location updates

**7. Design Google Search**
Key: Crawling, inverted index, PageRank

**8. Design Amazon/E-commerce**
Key: Product catalog, inventory, payment saga

**9. Design Dropbox/Google Drive**
Key: File chunking, sync, deduplication

**10. Design Rate Limiter**
Key: Token bucket, sliding window, distributed counting

**11. Design Notification System**
Key: Multi-channel, priority, aggregation, user preferences

**12. Design Typeahead/Autocomplete**
Key: Trie, caching, ranking by frequency

**13. Design Web Crawler**
Key: BFS/DFS, politeness, deduplication, priority

**14. Design Ticketmaster/Booking System**
Key: Seat locking, distributed locks, consistency

**15. Design Pastebin**
Key: Similar to URL shortener + text storage

**16. Design Parking Lot System**
Key: Object-oriented design, real-time availability

**17. Design Facebook Messenger**
Key: Group chat, online status, message ordering

**18. Design Hotel Booking (like Airbnb)**
Key: Search, availability calendar, booking saga

**19. Design News Feed (Facebook)**
Key: Ranking algorithm, pre-computation, personalization

**20. Design Cache System (like Memcached)**
Key: Eviction policies, consistent hashing, distributed architecture

### Quick Approach for Each
For ANY question, always start with:
1. What are we building? (Scope)
2. For how many people? (Scale)
3. What's most important? (Requirements)
4. Then design accordingly!

---


## DAY 93: Design a Distributed Cache (Redis Architecture)

### Requirements
- Store key-value pairs in memory (RAM)
- Sub-millisecond reads and writes
- Support millions of operations per second
- Handle node failures gracefully
- Scale horizontally (add more servers)
- Support data expiration (TTL)
- Eviction when memory is full

### Architecture
```
[Application Servers]
        |
[Cache Client Library]
        |
[Consistent Hashing Ring]
        |
[Cache Node 1]  [Cache Node 2]  [Cache Node 3]
(Master+Replica) (Master+Replica) (Master+Replica)
```

### Key Design Decisions

**Data Distribution: Consistent Hashing**
```
hash(key) -> position on ring -> next clockwise node
- Adding/removing node: Only 1/N of keys need to move
- Virtual nodes for even distribution
```

**Eviction Policies (When Memory is Full)**
- **LRU** (Least Recently Used): Remove what hasn't been used longest
- **LFU** (Least Frequently Used): Remove what's used least often
- **TTL** (Time To Live): Remove expired items first
- **Random**: Just pick a random key to remove

**Replication**
```
Master handles writes -> Async replicates to slave
If master dies -> Promote slave to new master (automatic)
Sentinel/Cluster mode for automatic failover
```

### Cache Patterns Review
```
1. Cache-Aside: App manages cache manually
2. Write-Through: Write cache + DB simultaneously
3. Write-Behind: Write cache, async write to DB
4. Read-Through: Cache fetches from DB on miss
```

### Memory Trick
**CACHE DESIGN = Consistent hashing, Available always, Clean when full, Hit rate matters, Evict wisely**

---

## DAY 94: Design a Distributed File System (like GFS/HDFS)

### Requirements
- Store files that are hundreds of MB to several GB
- Handle thousands of concurrent reads
- Optimized for large sequential reads (not random access)
- Fault tolerant (data survives hardware failures)
- Scale to petabytes of data

### Architecture (Google File System / HDFS)
```
[Client]
    |
[Master (NameNode)] - Stores metadata: file names, locations, permissions
    |
[Chunk Servers (DataNodes)] - Store actual file data

File "video.mp4" (300MB):
- Split into chunks: Chunk 1 (64MB), Chunk 2 (64MB), ... Chunk 5 (44MB)
- Each chunk stored on 3 different servers (replication factor = 3)
- Master knows: Chunk 1 is on Server A, B, D
                Chunk 2 is on Server B, C, E
                ...
```

### Read Flow
```
1. Client asks Master: "Where is video.mp4?"
2. Master replies: "Chunks 1-5, here are their locations"
3. Client reads directly from Chunk Servers (no bottleneck on Master!)
4. Client can read different chunks from different servers in parallel
```

### Write Flow
```
1. Client asks Master: "I want to write new_file.txt"
2. Master allocates chunks, picks 3 servers per chunk
3. Client sends data to first server
4. First server replicates to second, second to third (pipeline)
5. All confirm -> Write successful!
```

### Handling Failures
- **Chunk Server dies**: Master detects via heartbeat, re-replicates chunks from other copies
- **Master dies**: Standby master takes over (has replicated metadata)
- **Data corruption**: Checksums verify integrity, re-fetch from another copy

### Memory Trick
**GFS = Giant Files Spread (across many machines with copies)**

---

## DAY 95: Design a Job Scheduler (like Cron at Scale)

### Requirements
- Schedule jobs to run at specific times or intervals
- Handle millions of scheduled tasks
- Exactly-once execution (don't run job twice!)
- Handle worker failures
- Priority levels
- Job dependencies (Job B runs only after Job A completes)

### Architecture
```
[Job Submission API] --> [Job Queue (Priority)] --> [Scheduler]
                                                       |
                              [Worker Pool: Worker 1, Worker 2, ... Worker N]
                                                       |
                              [Job State Store: pending, running, completed, failed]
```

### How It Works
```
1. User creates job: "Run backup every day at 2 AM"
2. Scheduler stores: {job_id: 1, next_run: "2AM tomorrow", repeat: "daily"}
3. Every minute, Scheduler checks: "Any jobs due NOW?"
4. If yes: Put job in queue
5. Worker picks up job, executes it
6. Worker reports: Success or Failure
7. If daily: Scheduler calculates next run time
```

### Handling Failures
```
Worker starts job, then crashes:
- Job has "heartbeat timeout" (e.g., 5 minutes)
- If no heartbeat for 5 min -> Mark job as FAILED
- Retry policy: Try again (max 3 attempts)
- After 3 failures: Alert operations team

Scheduler crashes:
- Multiple scheduler instances (leader election)
- If leader dies, new leader takes over
```

### Exactly-Once Execution
```
Problem: Two schedulers might trigger same job!
Solution: Distributed lock on job_id
- Before running: Acquire lock on "job:123"
- If lock acquired: Run the job
- If lock failed: Someone else got it, skip
```

### Key Design Decisions
- Timer: Redis sorted sets (score = next execution time)
- State: PostgreSQL (reliable storage of job definitions)
- Queue: Kafka or RabbitMQ (reliable task distribution)
- Workers: Stateless (can be added/removed easily)
- Locks: Redis or ZooKeeper for distributed locks

---

## DAY 96: Design a Metrics/Monitoring System (like Prometheus)

### Requirements
- Collect metrics from thousands of services
- Store time-series data efficiently
- Query: "What was CPU usage of server X from 3-4 PM?"
- Dashboards with real-time graphs
- Alerting when metrics exceed thresholds
- Retain data for months/years
- Handle millions of data points per second

### Architecture
```
[Services: expose metrics]
        |
[Collectors/Scrapers: pull metrics every 15s]
        |
[Time-Series Database]
        |
[Query Engine] --> [Dashboard (Grafana)]
        |
[Alert Engine] --> [Notification (PagerDuty)]
```

### Data Model
```
Metric: http_requests_total
Labels: {method="GET", path="/api/users", status="200"}
Values: (timestamp, value) pairs

Example data points:
(1625000000, 15234)
(1625000015, 15289)  (+55 requests in 15 seconds)
(1625000030, 15301)  (+12 requests in 15 seconds)
```

### Time-Series Storage Optimizations
```
1. Delta encoding: Store differences, not absolute values
   Values: 15234, 15289, 15301
   Stored: 15234, +55, +12  (much smaller!)

2. Downsampling: As data ages, reduce resolution
   Last 24h: Every 15 seconds (high res)
   Last week: Every 1 minute (medium res)
   Last year: Every 1 hour (low res)

3. Compression: Column-oriented storage
   All timestamps together, all values together
   Better compression ratio!
```

### Alerting Engine
```
Rules defined:
- IF avg(cpu_usage{server="web-1"}) > 90% FOR 5min THEN alert
- IF rate(http_errors) / rate(http_total) > 0.05 THEN page

Processing:
1. Evaluate each rule every 15 seconds
2. If condition true: Start timer
3. If condition true for configured duration: Fire alert!
4. Send to notification channel
```

### Memory Trick
**METRICS = Measurements Enabling Tracking Real Issues Continuously in Systems**

---


## DAY 97: Design a Recommendation System

### Requirements
- Suggest relevant content/products to users
- Handle millions of users and millions of items
- Real-time (respond within 100ms)
- Continuously improve based on user behavior
- Handle cold start (new users with no history)

### Types of Recommendations

**1. Collaborative Filtering**
```
"Users similar to you liked these items"
User A likes: [Movie1, Movie3, Movie5]
User B likes: [Movie1, Movie3, Movie7]
A and B are similar! Recommend Movie7 to A, Movie5 to B.
```

**2. Content-Based**
```
"Items similar to what you've liked"
User likes: Action movies with Tom Cruise
Recommend: Other action movies, other Tom Cruise movies
```

**3. Hybrid (Best approach)**
```
Combine collaborative + content-based + popularity
Score = 0.4 × collaborative + 0.3 × content + 0.2 × popularity + 0.1 × freshness
```

### Architecture
```
[User Activity] --> [Event Stream (Kafka)]
                         |
              [Real-time Features] --> [Feature Store]
                         |                    |
              [ML Model Training (Batch)]     |
                         |                    |
              [Model Store]                   |
                         |                    |
[User Request] --> [Recommendation Service] --> [Candidate Generation]
                                            --> [Ranking Model]
                                            --> [Re-ranking & Filtering]
                                            --> [Top N Results]
```

### Two-Stage Approach (How Netflix/YouTube Does It)
```
Stage 1: Candidate Generation (broad, fast)
- From millions of items, find ~1000 candidates
- Use simple models (collaborative filtering)
- Speed: Must be fast (<20ms)

Stage 2: Ranking (precise, slower)
- From 1000 candidates, rank by relevance
- Use complex ML model with many features
- Consider: recency, diversity, user context
- Return top 20-50 items
```

### Handling Cold Start
- **New user**: Show popular items, ask preferences during signup
- **New item**: Use content features (genre, description, similar items)
- **As user interacts**: Gradually shift to personalized recommendations

### Memory Trick
**RECOMMEND = Recall candidates, Estimate scores, Combine methods, Order by relevance, Mix in diversity, Make it personal, Evaluate results, New data improves, Deliver fast**

---

## DAY 98: Design a Distributed Transaction System

### The Big Idea
When a transaction spans multiple services/databases, how do you ensure ALL parts succeed or ALL parts fail? This is the hardest problem in distributed systems!

### Two-Phase Commit (2PC)
```
Phase 1: PREPARE
Coordinator: "Can you commit?" --> Service A: "Yes!" (VOTE)
Coordinator: "Can you commit?" --> Service B: "Yes!" (VOTE)
Coordinator: "Can you commit?" --> Service C: "Yes!" (VOTE)

Phase 2: COMMIT (only if ALL said yes)
Coordinator: "COMMIT!" --> Service A: Done!
Coordinator: "COMMIT!" --> Service B: Done!
Coordinator: "COMMIT!" --> Service C: Done!

If ANY said "No" in Phase 1:
Coordinator: "ABORT!" --> All services rollback
```

### Problems with 2PC
- **Blocking**: If coordinator dies between phases, participants wait forever
- **Single Point of Failure**: Coordinator is critical
- **Performance**: Holding locks during entire protocol is slow

### Three-Phase Commit (3PC)
Adds a "pre-commit" phase to reduce blocking:
```
Phase 1: Can Commit? (VOTE)
Phase 2: Pre-Commit (PREPARE - but don't commit yet)
Phase 3: Do Commit (ACTUALLY commit)
```
- If coordinator dies after Phase 2, participants can decide themselves
- Less blocking, but more messages

### Modern Alternative: Saga Pattern (Revisited)
```
Instead of distributed transaction:
Execute steps in sequence, compensate on failure.

Step 1: Debit Account A ($100)
Step 2: Credit Account B ($100)

If Step 2 fails:
Compensate Step 1: Credit Account A ($100) (undo the debit)
```

### Comparison
| Approach | Consistency | Performance | Complexity |
|----------|------------|-------------|------------|
| 2PC | Strong | Slow (blocking) | Medium |
| 3PC | Strong | Better | High |
| Saga | Eventual | Fast | Medium |
| Event Sourcing | Eventual | Fast | High |

### When to Use What
- **2PC**: When you MUST have strong consistency (banking between systems)
- **Saga**: When eventual consistency is acceptable (e-commerce orders)
- **Event Sourcing**: When you need audit trail + eventual consistency

### Memory Trick
**2PC = Two Phases: First ask, then act (or abort)**

---

## DAY 99: Putting It All Together - Full Design Exercise

### Design Challenge: Build "SuperApp" (like WeChat/Grab)

A super app that combines:
- Messaging
- Payments
- Food Delivery
- Ride Hailing
- Social Feed

### Step 1: Requirements
```
Users: 100M DAU
Features: Chat, Pay, Order Food, Ride, Social
Priorities: Reliability (payments), Speed (chat), Scale (social)
```

### Step 2: High-Level Architecture
```
[Mobile App (Single App)]
         |
[API Gateway + Auth]
         |
[Service Mesh]
         |
+--------+--------+--------+--------+--------+
|        |        |        |        |        |
[Chat]  [Payment] [Food]  [Ride]  [Social] [User]
[Service][Service][Service][Service][Service][Service]
         |
[Shared Infrastructure]
- Event Bus (Kafka)
- Caching Layer (Redis Cluster)
- Object Storage (S3)
- Monitoring (Prometheus + Grafana)
- Service Discovery (Consul)
```

### Step 3: Database Strategy
```
Chat: Cassandra (high write throughput, time-series)
Payment: PostgreSQL (ACID, strong consistency)
Food Orders: MongoDB (flexible schema, varies by restaurant)
Ride: Redis (real-time locations) + PostgreSQL (trip history)
Social: Cassandra (feed) + Elasticsearch (search) + Neo4j (connections)
User: PostgreSQL (master data)
```

### Step 4: Cross-Cutting Concerns
```
Authentication: JWT + OAuth2 (single sign-on across all services)
Rate Limiting: Per-user, per-service, per-endpoint
Logging: Centralized (ELK Stack)
Tracing: Distributed tracing (Jaeger) - track request across services
Feature Flags: Gradual rollout of new features
A/B Testing: Test different experiences
```

### Step 5: Scalability Plan
```
Scaling Strategy per Service:
- Chat: Horizontal (add WebSocket servers)
- Payment: Vertical + Read replicas (reliability > scale)
- Food: Horizontal (geographic sharding by city)
- Ride: Horizontal (geographic sharding + Redis cluster)
- Social: Horizontal (sharded by user_id)
```

### Step 6: Failure Handling
```
- Circuit breakers between all services
- Bulkheads (isolated thread pools)
- Graceful degradation (if social feed is down, other features work)
- Multi-region active-active for chat and payments
- Saga pattern for cross-service transactions
- Chaos engineering for testing resilience
```

---


## DAY 100: Final Review & Cheat Sheet

### Congratulations! You've completed 100 days of System Design!

### The Ultimate System Design Cheat Sheet

#### 1. SCALING
| Problem | Solution |
|---------|----------|
| Too many users | Horizontal scaling + Load balancer |
| Slow database reads | Read replicas + Caching |
| Too much data | Sharding |
| Global users | CDN + Multi-region |
| Spiky traffic | Auto-scaling + Queue |

#### 2. DATA STORAGE
| Need | Technology |
|------|-----------|
| Structured + ACID | PostgreSQL |
| Flexible documents | MongoDB |
| Lightning fast cache | Redis |
| Massive writes | Cassandra |
| Full-text search | Elasticsearch |
| Social graph | Neo4j |
| Time-series metrics | InfluxDB / TimescaleDB |
| File/Media storage | S3 / Object Storage |
| Event streaming | Kafka |

#### 3. COMMUNICATION
| Pattern | When |
|---------|------|
| REST API | Standard client-server |
| GraphQL | Flexible data fetching |
| gRPC | Fast inter-service |
| WebSocket | Real-time bidirectional |
| Message Queue | Async processing |
| Pub/Sub | Event notifications |

#### 4. KEY PATTERNS
| Pattern | Solves |
|---------|--------|
| Load Balancer | Traffic distribution |
| Cache | Speed (reads) |
| CDN | Geographic speed |
| Queue | Decoupling + Async |
| Sharding | Data size |
| Replication | Reliability + Read speed |
| Circuit Breaker | Cascading failures |
| Saga | Distributed transactions |
| CQRS | Read/Write optimization |
| Event Sourcing | Audit + Rebuild state |

#### 5. NUMBERS TO KNOW
```
QPS for "1 million users":
- If each user makes 10 requests/day:
  10M requests/day ÷ 100K seconds = ~100 QPS

Storage for "1 million users":
- 1KB per user profile = 1 GB
- 1 photo (1MB) per user = 1 TB

Latency targets:
- Page load: < 2 seconds
- API response: < 200ms
- Real-time: < 100ms
- Database query: < 50ms
```

#### 6. THE DESIGN FRAMEWORK (Always Follow This)
```
1. CLARIFY requirements (5 min)
2. ESTIMATE scale (5 min)
3. DESIGN high-level (10 min)
4. DEEP DIVE into key components (15 min)
5. DISCUSS trade-offs & scalability (10 min)
```

#### 7. TRADE-OFFS QUICK REFERENCE
```
Consistency vs Availability (pick based on use case)
SQL vs NoSQL (structure vs flexibility)
Monolith vs Microservices (simplicity vs scalability)
Cache vs Fresh Data (speed vs accuracy)
Sync vs Async (immediate vs eventual)
Vertical vs Horizontal (simple vs unlimited)
Push vs Pull (server effort vs client effort)
Strong vs Eventual consistency (accuracy vs speed)
```

### Final Memory Trick: The System Design Alphabet

**A** - API Design, Availability
**B** - Bloom Filters, Batching
**C** - Caching, CDN, CAP Theorem, Consistent Hashing
**D** - Database (SQL/NoSQL), DNS, Distributed Systems
**E** - Event-Driven, Elasticsearch, Encryption
**F** - Failover, Fault Tolerance, Fan-out
**G** - Geospatial, Gossip Protocol, gRPC
**H** - Horizontal Scaling, Hashing, Heartbeat
**I** - Indexing, Idempotency, ID Generation
**J** - JSON, Job Scheduling
**K** - Kafka, Key-Value Stores
**L** - Load Balancer, Latency, Logging
**M** - Microservices, Message Queue, Monitoring
**N** - Notification System, Network Protocols
**O** - Object Storage, Orchestration
**P** - Partitioning, Pub/Sub, Proxies
**Q** - Queue, Query Optimization
**R** - Replication, Rate Limiting, Redis
**S** - Sharding, Saga, Search, Streaming
**T** - TCP/UDP, Throughput, Trade-offs
**U** - UUID/Unique IDs, URL Shortener
**V** - Vertical Scaling, Virtual Nodes
**W** - WebSocket, Write-Ahead Log
**X** - XSS Protection
**Y** - YAML configs
**Z** - ZooKeeper, Zero-downtime deployment

---

### Your 100-Day Journey Summary

| Phase | Days | Focus |
|-------|------|-------|
| Foundation | 1-20 | Core building blocks |
| Core Concepts | 21-40 | Patterns & principles |
| Building Blocks | 41-60 | Advanced components |
| Real Designs | 61-85 | Famous system walkthroughs |
| Interview Prep | 86-100 | Putting it all together |

### What's Next?
1. **Practice**: Pick 3 design questions per week and practice with a friend
2. **Read**: System design blogs (Engineering at Netflix, Uber, etc.)
3. **Build**: Create a small distributed system yourself
4. **Teach**: Explain these concepts to others (best way to learn!)
5. **Stay Updated**: Follow tech blogs for new patterns and tools

### Golden Advice
> "The best system designers don't memorize architectures - they understand TRADE-OFFS. Every design decision has a cost and a benefit. Know them, and you can design anything."

---

**Thank you for completing this course! You now have the knowledge to design systems that serve millions of users. Go build something amazing!**

---

*End of Course*

GET / - redirect to /news

News Routes:
GET /news - list of most recent news
GET /news/:news_id - get news by ID

News:
- Party Name who posted - PartyID
- Post Date - Date
- Theme - ThemeID
- Rating - int
- Image/video? - link
- Comments array - Comment[]

Comment:
- Author - User
- Message - string
- Rating - int
- responses? - Comment[]

Party 
GET /party/:party_name - get party profile 

Party Profile Object:
- Party Icon - link
- Short Description - string
- Link to some official website? - string
- Most Recent Posts - News[]
- List of Users from this Party? - User[]

User:
- Name - string
- Registration Date - Date
- Profile Picture? - link
- Short Description - string
- Party that they are in? - PartyID
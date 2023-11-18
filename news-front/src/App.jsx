import './App.css'
import Nav from './components/nav/nav.jsx'
import {BrowserRouter, Routes , Route } from 'react-router-dom';
function App() {

  return (
    <BrowserRouter>
      <div className="App">
        <div className="wrapper">
          <Header />
          <div className='page'>
            <Nav />
            <Routes>
              <Route path="/newsfeed" element={<NewsFeed/>}/>
              <Route path="/forum" element={<Forum/>} />
              <Route path="/party" element={<Forum/>} />
            </Routes>
            {/*<Gallery />*/}
            {/*<Chat />*/}
          </div>
        </div>
      </div>
      </BrowserRouter>
  );

}

export default App

import React from 'react';
import nav_style from './nav.module.css';
function nav_component(){
    return (
      <nav className={nav_style.nav}>
        <div>
          <ul>
            <li><NavLink to='/newsfeed'>News Feed</NavLink></li>
            <li><NavLink to='/forum'>Forum</NavLink></li>
            <li><NavLink to='/party'>Parties</NavLink></li>
          </ul>
        </div>
      </nav>
    )
      
      
}
export default nav_component;
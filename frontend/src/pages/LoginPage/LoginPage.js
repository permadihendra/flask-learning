import React from 'react';

const LoginPage = () => {
  return (

    <div className="signUpContainer">
    <form>
    <h2>Login</h2>
      <div className="signUpForm">
        <label htmlFor="name">Name</label>
        <input id="name" type="text"  name="name" />

      <label htmlFor="email">Email Address</label>
        <input id="email" type="email"  name="email" />

       <label htmlFor="password">Password</label>
        <input  id="password" type="password" name="password"  />
            <button>Login</button>
			      </div>

    </form>
    </div>

  );
};

export default LoginPage;
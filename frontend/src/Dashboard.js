import React, {useState} from "react";

const Dashboard = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    
    const handleLogin = () => {
        setIsLoggedIn(true);
    }

    const handleLogout = () => {
        setIsLoggedIn(false);
    }

    return (
        <div>
            {isLoggedIn ? (
                <button onClick={handleLogout}>Logout</button>
            ) : (
                <button onClick={handleLogin}>Login</button>
            )}
            { isLoggedIn && <p>Hey Friend, Welcome</p>}
            { !isLoggedIn && <p>Please log in to continue</p>}
        </div>
    );
}

export default Dashboard;
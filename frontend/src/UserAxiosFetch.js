import { useEffect, useState } from "react";
import axios from 'axios'

const UserAxiosFecth = () => {
    const [data, setData] = useState([]);

    const APP_URL = 'https://jsonplaceholder.typicode.com/users';

    const getSpeaker = () => {
        axios.get(APP_URL)
        .then(response => {
            setData(response.data)
        })
    }

    useEffect(() => {
        getSpeaker();
    }, []);

    return (
        <>
            <h1>Speaker Information - Axios fetch API</h1>
            <ul>
                {data.map(speaker => (
                    <li key={speaker.id}>
                        {speaker.name}, <em>
                        {speaker.email} </em>
                    </li>
                )
                )}
            </ul>
        </>
    );

};

export default UserAxiosFecth;
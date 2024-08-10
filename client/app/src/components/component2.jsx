import React, {useState, useEffect} from "react";
import axios from 'axios';


const Component2 = () => {

    const [Data, SetData] = useState(null);

    const fetchData = async() => {
        
        try{

            const response = await axios.get(`http://127.0.0.1:8000/user/dev2`);
            console.log(response.data);
            SetData(response.data);

        }catch(error){
            console.log(`Error in Component2 @fetchData function, ${error}`);
        }
    }

    const [UserArray, SetUserArray] = useState([]);

    const fetchUsers = async() => {

        try{

            const response = await axios.get(`http://127.0.0.1:8000/user/show/users`);
            console.log(response.data);
            SetUserArray(response.data);

        }catch(error){
            console.log(`Error in Component2 @fetchUsers funtion, ${error}`);
        }
    }


    useEffect(() => {
        fetchData();
        fetchUsers();
    }, [])

    return ( 
        <>
            <h1>This is Component2</h1>
            {Data && (<h3>{Data.developer_email}</h3>)}

            {UserArray.map((UserInstance) => (
                <div>
                    <p>{UserInstance.first_name}</p>
                    <p>{UserInstance.date_joined}</p>
                </div>
            ))}
        </>
    )
}

export default Component2;
import React, {useEffect, useState} from 'react';

const SignUp = () => {

    // const [name, setName] = useState("");
    // const [email, setEmail] = useState("");
    // const [password, setPassword] = useState("");
    // const nameHandler = (e) => {
    //     setName(e.target.value);
    // };

    // const emailHandler = (e) => {
    //     setEmail(e.target.value);
    // }

    // const passwordHandler = (e) => {
    //     setPassword(e.target.value);
    // }


    // Form Validations
    const initialValues = { name: "", email: "", password: ""}
    const [formValues, setFormValues] = useState(initialValues);
    const [formErrors, setFormErrors] = useState({});
    const [isSubmit, setIsSubmit] = useState(false);

    const onChangeHandler = (e) => {
        const {name, value} = e.target;
        setFormValues({ ...formValues, [name]: value});
    }
    
    useEffect(() => {
        if (Object.keys(formErrors).length === 0 && isSubmit ){
           console.log(formValues);
        }  
    }, [formErrors, formValues, isSubmit]);

    const validateForm = (values) => {
        const errors = {};
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;
        if (!values.name) {
            errors.name = "Name is required!";
        }

        if (!values.email) {
            errors.email = "Email is required!";
        } else if (!regex.test(values.email)) {
            errors.email = "Invalid email format!";
        }
        
        if (!values.message) {
            errors.message = "Message is required!";
        }
        
        return errors;

    }

    const onSubmitHandler = (e) => {
        e.preventDefault();
        // alert(`Name: ${name}: Email: ${email} Password: ${password}`);
        const errors = validateForm(formValues)
        setFormErrors(errors);
        setIsSubmit(true);

        if (Object.keys(errors).length === 0) {
            // No errors — proceed to submit or send data
            console.log("Form Submitted", formValues);
        } else {
            console.log("Validation Errors", errors);
        }
    };

    return (

        <div className="signUpContainer">
        <form onSubmit={onSubmitHandler}>
        <h2>Create an Account</h2>
        <div className="signUpForm">
            <label htmlFor="name">Name</label>
            <p style={{ color: 'red', fontWeight: 'bold' }}>
                {formErrors.name}
            </p>
            <input 
                id="name" 
                type="text"  
                name="name" 
                value={formValues.name} 
                onChange={onChangeHandler}/>

        <label htmlFor="email">Email Address</label>
            <p style={{ color: 'red', fontWeight: 'bold' }}>
                {formErrors.email}
            </p>
            <input 
                id="email" 
                type="email"  
                name="email" 
                value={formValues.email}
                onChange={onChangeHandler}
                />

        <label htmlFor="password">Password</label>
            <p style={{ color: 'red', fontWeight: 'bold' }}>
                {formErrors.password}
            </p>
            <input  
                id="password" 
                type="password" 
                name="password"  
                value={formValues.password}
                onChange={onChangeHandler}
                />
                
                <button>Register</button>
                    </div>

        </form>
        </div>

    );
};

export default SignUp;
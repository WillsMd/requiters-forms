# **Recruitment API**

This Recruitment API allows users to submit and manage recruitment data, such as personal details, skills, motivations, and project descriptions. It is built with Django and integrates seamlessly with frontend applications like React.

---

## **API Overview**

### **Base URL**
The API is hosted at:  
`https://your-api-domain.com/`

---

## **Features**

1. Submit and manage user data (e.g., name, registration number, department).
2. Associate additional questions and answers with each user:
   - Clubs (list of strings).
   - Motivation.
   - Skills (list of strings).
   - Explanation of a big project or solution.
   - Reason to join.
   - GitHub profile link (optional).
   - Selected picture choice (string).
3. Fully RESTful API designed for integration with React or other frontend frameworks.

---

## **Endpoints**

### **1. Create a User**
**POST** `/api/users/`

#### Request Body:
```json
{
    "fname": "Mtu",
    "mname": "Mbadi",
    "lname": "Sana",
    "regno": "xxxx-xx-xxxxx",
    "department": "ETE"
}
```

#### Response:
```json
{
    "id": 1,
    "fname": "Mtu",
    "mname": "Mbadi",
    "lname": "Sana",
    "regno": "xxxx-xx-xxxxx",
    "department": "ETE"
}
```

---

### **2. Create Questions for a User**
**POST** `/api/questions/`

#### Request Body:
```json
{
    "user": 1,
    "clubs": ["Photography", "Coding"],
    "motivation": "I want to contribute to impactful projects.",
    "skills": ["Python", "React", "Problem Solving"],
    "picture_choice": "picture1",
    "github_link": "https://github.com/example",
    "big_project": "Built a real-time chat application.",
    "reason_to_join": "To work on meaningful projects and grow my skills."
}
```

#### Response:
```json
{
    "id": 1,
    "user": 1,
    "clubs": ["Photography", "Coding"],
    "motivation": "I want to contribute to impactful projects.",
    "skills": ["Python", "React", "Problem Solving"],
    "picture_choice": "picture1",
    "github_link": "https://github.com/example",
    "big_project": "Built a real-time chat application.",
    "reason_to_join": "To work on meaningful projects and grow my skills."
}
```

---

### **3. Retrieve a User with Questions**
**GET** `/api/users/<id>/`

#### Response:
```json
{
    "id": 1,
    "fname": "John",
    "mname": "Doe",
    "lname": "Smith",
    "regno": "ETE123456789",
    "department": "ETE",
    "questions": {
        "id": 1,
        "clubs": ["Photography", "Coding"],
        "motivation": "I want to contribute to impactful projects.",
        "skills": ["Python", "React", "Problem Solving"],
        "picture_choice": "picture1",
        "github_link": "https://github.com/example",
        "big_project": "Built a real-time chat application.",
        "reason_to_join": "To work on meaningful projects and grow my skills."
    }
}
```

---

## **React Integration Example**

Below is an example of how to connect to this API using React.

### **1. Install Axios**
```bash
npm install axios
```

### **2. React Code Examples**

#### **Create a User**
```jsx
import axios from 'axios';

const createUser = async (userData) => {
    try {
        const response = await axios.post('https://your-api-domain.com/api/users/', userData);
        console.log('User created:', response.data);
    } catch (error) {
        console.error('Error creating user:', error.response?.data || error.message);
    }
};

// Example usage
const newUser = {
    fname: "Mtu",
    mname: "Mbadi",
    lname: "Sana",
    regno: "xxxx-xx-xxxxx",
    department: "ETE"
};
createUser(newUser);
```

---

#### **Create Questions for a User**
```jsx
const createQuestions = async (userId, questionData) => {
    try {
        const response = await axios.post('https://your-api-domain.com/api/questions/', {
            ...questionData,
            user: userId,
        });
        console.log('Questions created:', response.data);
    } catch (error) {
        console.error('Error creating questions:', error.response?.data || error.message);
    }
};

// Example usage
const newQuestions = {
    clubs: ["Photography", "Coding"],
    motivation: "I want to contribute to impactful projects.",
    skills: ["Python", "React", "Problem Solving"],
    picture_choice: "picture1",
    github_link: "https://github.com/example",
    big_project: "Built a real-time chat application.",
    reason_to_join: "To work on meaningful projects and grow my skills."
};
createQuestions(1, newQuestions);
```

---

#### **Retrieve a User with Questions**
```jsx
const getUserWithQuestions = async (userId) => {
    try {
        const response = await axios.get(`https://your-api-domain.com/api/users/${userId}/`);
        console.log('User details:', response.data);
    } catch (error) {
        console.error('Error retrieving user:', error.response?.data || error.message);
    }
};

// Example usage
getUserWithQuestions(1);
```

---

## **Data Format**
### **Skills and Clubs**
- **Skills**: Provide as an array of strings. Example: `["Python", "React", "Problem Solving"]`.
- **Clubs**: Provide as an array of strings. Example: `["Photography", "Coding"]`.

### **Picture Choices**
- Pictures are handled in the frontend, and you only need to pass the picture name, e.g., `"picture1"`, `"picture2"`, etc.

---
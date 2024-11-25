# **Recruitment API**

The Recruitment API enables users to register and provide additional information such as their skills, motivations, projects they want to join, and other relevant data. This API is designed for seamless integration with frontend frameworks like React.

---

## **API Overview**

### **Base URL**
The API is hosted at:  
`https://your-api-domain.com/`

---

## **Features**

1. **Dynamic Project Management**:
   - Admins can add, edit, or remove projects dynamically through the admin interface.
   - Users select a project to join from the available list.

2. **User Information**:
   - Basic personal details (first name, last name, middle name, course, and year of study).

3. **Additional Questions**:
   - Clubs (as a list, or "None"/"Other" for descriptions).
   - Motivation for joining.
   - Skills (list of strings).
   - Explanation of a big project or solution.
   - Reason to join.

4. Fully RESTful API for backend/frontend integration.

---

## **Endpoints**

### **1. Create a User**
**POST** `/api/users/`

#### Request Body:
```json
{
    "fname": "Jane",
    "mname": "Doe",
    "lname": "Smith",
    "course": "CEIT",
    "year_of_study": 3
}
```

#### Response:
```json
{
    "id": 1,
    "fname": "Jane",
    "mname": "Doe",
    "lname": "Smith",
    "course": "CEIT",
    "year_of_study": 3
}
```

---

### **2. Create Questions for a User**
**POST** `/api/questions/`

#### Request Body:
```json
{
    "user": 1,
    "project": 2,
    "clubs": ["Photography", "Coding"],
    "motivation": "I want to contribute to impactful projects.",
    "skills": ["Python", "Django", "Problem Solving"],
    "big_project": "Created an energy management system.",
    "reason_to_join": "To grow my skills and work on meaningful projects."
}
```

#### Response:
```json
{
    "id": 1,
    "user": 1,
    "project": 2,
    "clubs": ["Photography", "Coding"],
    "motivation": "I want to contribute to impactful projects.",
    "skills": ["Python", "Django", "Problem Solving"],
    "big_project": "Created an energy management system.",
    "reason_to_join": "To grow my skills and work on meaningful projects."
}
```

---

### **3. Retrieve a User with Questions**
**GET** `/api/users/<id>/`

#### Response:
```json
{
    "id": 1,
    "fname": "Jane",
    "mname": "Doe",
    "lname": "Smith",
    "course": "CEIT",
    "year_of_study": 3,
    "questions": {
        "id": 1,
        "project": "Energy",
        "clubs": ["Photography", "Coding"],
        "motivation": "I want to contribute to impactful projects.",
        "skills": ["Python", "Django", "Problem Solving"],
        "big_project": "Created an energy management system.",
        "reason_to_join": "To grow my skills and work on meaningful projects."
    }
}
```

---

### **4. Create/Manage Projects**
Admins can manage the projects dynamically through the admin interface:
- Add new projects.
- Edit project names.
- Delete unused projects.

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
    fname: "Jane",
    mname: "Doe",
    lname: "Smith",
    course: "CEIT",
    year_of_study: 3
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
    project: 2, // Project ID
    clubs: ["Photography", "Coding"],
    motivation: "I want to contribute to impactful projects.",
    skills: ["Python", "Django", "Problem Solving"],
    big_project: "Created an energy management system.",
    reason_to_join: "To grow my skills and work on meaningful projects."
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
- **Skills**: Provide as an array of strings. Example: `["Python", "Django", "React"]`.
- **Clubs**: Provide as an array of strings. If not in any club, enter `"None"`. For other descriptions, use `"Other"` and add a custom description.

### **Projects**
- Projects are managed dynamically via the admin interface.
- Pass the project ID when submitting questions.

---

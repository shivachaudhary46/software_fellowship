const API_BASE = "http://127.0.0.1:8000";

async function fetchTodos() {
  const res = await fetch(`${API_BASE}/`);
  const todos = await res.json();

  const list = document.getElementById("todo-list");
  list.innerHTML = "";

  todos.forEach(todo => {
    const li = document.createElement("li");
    li.innerText = `#${todo.id}: ${todo.title} - ${todo.completed ? "✅" : "❌"}`;
    list.appendChild(li);
  });
}

async function addTodo() {
  const id = document.getElementById("todo-id").value;
  const title = document.getElementById("todo-title").value;
  const completed = document.getElementById("todo-completed").checked;

  const todo = { id: parseInt(id), title, completed };

  const res = await fetch(`${API_BASE}/create-todo`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(todo)
  });

  if (res.ok) {
    alert("✅ Todo Added!");
    fetchTodos();
  } else {
    const err = await res.json();
    alert("❌ Error: " + err.detail);
  }
}

async function getTodoById() {
  const id = document.getElementById("search-id").value;

  if (!id) {
    alert("Enter a valid ID");
    return;
  }

  const res = await fetch(`${API_BASE}/get-todo/${id}`);
  const list = document.getElementById("todo-list");
  list.innerHTML = "";

  if (res.ok) {
    const todo = await res.json();
    const li = document.createElement("li");
    li.innerText = `#${todo.id}: ${todo.title} - ${todo.completed ? "✅" : "❌"}`;
    list.appendChild(li);
  } else {
    alert("Todo not found");
  }
}

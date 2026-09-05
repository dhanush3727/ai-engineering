# Sets
numbers = {1,2,3,4,5,1}
print(numbers)
print(type(numbers))

languages = ["Python", "JS", "JS", "TypeScript"]
print(languages)
unique = set(languages)
print(unique)

# Adding values
numbers.add(6)
print(numbers)

# Removing values
numbers.remove(3) # Error if value doesn't exist
print(numbers)
numbers.discard(7) # Doesn't error if value doesn't exist
print(numbers)

# Checking values
print(1 in numbers) # True
print(3 in numbers) # False

# Set operations
frontend = {"React.js", "Next.js", "JavaScript", "TypeScript"}
backend = {"Node.js", "Express.js", "JavaScript", "TypeScript"}
# Union - Everything from both sets
all_technologies = frontend | backend
print(all_technologies)
# Intersection - Values common to both
common = frontend & backend
print(common)
# Difference - values in one set but not the other
frontend_only = frontend - backend
print(frontend_only)

# Exercise 1: Basic set
technologies = {"Python", "JavaScript", "TypeScript", "Python", "React", "JavaScript" }
print(len(technologies))
technologies.add("Next.js")
technologies.add("Python")
print("React" in technologies)
print("Rust" in technologies)
print(technologies)

# Exercise 2: 
skills = ["React", "Python", "React", "TypeScript", "Python", "NestJS", "React"]
unique_skills = set(skills)
print(unique_skills)

# Exercise 3: Set operations
frontend = {"React", "TypeScript", "Next.js", "Tailwind"}
backend = {"NestJS", "TypeScript", "PostgreSQL", "Next.js"}
all_technologies = frontend | backend
common_technologies = frontend & backend
frontend_only = frontend - backend
backend_only = backend - frontend
print(all_technologies)
print(common_technologies)
print(frontend_only)
print(backend_only)
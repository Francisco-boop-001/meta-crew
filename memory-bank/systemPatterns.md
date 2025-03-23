# System Patterns: Windows Development Environment

## Architecture Overview

```mermaid
flowchart TD
    PM[Package Manager] --> |Installs| Tools
    Tools --> |Configured via| ENV[Environment Variables]
    
    subgraph "Core Development Tools"
        VCS[Version Control - Git]
        Node[Node.js Runtime]
        Py[Python Ecosystem]
        Term[Terminal Tools]
    end
    
    subgraph "Environment Configuration"
        Path[PATH Variables]
        Config[Tool Configurations]
        Shells[Shell Setup]
    end
    
    Tools --> Core Development Tools
    ENV --> Environment Configuration
```

## Key Patterns

### Package Management
- Central package manager (Chocolatey, Scoop, or Winget) for simplified installation
- Direct installation only when package managers don't provide the tool
- Versioning handled through package manager when possible

### Environment Configuration
- PATH variables set correctly during installation
- Environment variables surfaced to all terminals/command prompts
- Consistent access to tools from any directory

### Shell Integration
- Command-line tools available in standard Windows shells
- Path configuration applied globally

### Tool Selection Philosophy
- Choose industry-standard tools with good Windows support
- Prefer tools with active maintenance
- Choose tools that integrate well with the Windows ecosystem

## Component Relationships
- Package managers serve as the foundation for installing other tools
- Version control (Git) works independently of other tools
- Programming languages (Node.js, Python) maintain their own package ecosystems
- Command-line tools extend the capabilities of the default Windows shells

# 📋 LongForm Video Platform - Versioning Strategy

## 🎯 **Version Control Overview**

**Current Version**: `v2.1.0`  
**Last Updated**: January 2, 2025  
**Versioning Scheme**: [Semantic Versioning (SemVer)](https://semver.org/)

---

## 📊 **Version Numbering System**

### **Format: MAJOR.MINOR.PATCH**

- **MAJOR** (X.0.0): Breaking changes, major new features, architecture changes
- **MINOR** (0.X.0): New features, enhancements, backward-compatible changes  
- **PATCH** (0.0.X): Bug fixes, documentation updates, minor improvements

### **Current Component Versions**

| Component | Version | Status | Last Updated |
|-----------|---------|--------|--------------|
| **Bible Chapter Generator** | `v2.1.0` | ✅ Production | Jan 2, 2025 |
| **Black Hebrew Israelite Workflow** | `v3.0.0` | ✅ Latest | Jan 2, 2025 |
| **Biblical Text Processor Script** | `v1.1.0` | ✅ Production | Jan 2, 2025 |
| **Scale Video Generator** | `v1.2.0` | ✅ Stable | Dec 25, 2024 |
| **Legacy Workflows** | `v1.0.0` | 📁 Archived | Dec 25, 2024 |
| **Documentation Suite** | `v2.1.0` | ✅ Current | Jan 2, 2025 |

---

## 📁 **New Folder Structure**

### **Recommended Reorganization**

```
LongForm_/
├── 🎬 PRODUCTION/                    # Active production systems
│   ├── bible-chapter-videos/         # v2.1.0 - Main biblical system
│   ├── black-hebrew-israelite/       # v3.0.0 - Latest specialized workflow
│   └── scale-video-generator/        # v1.2.0 - General video system
│
├── 📦 RELEASES/                      # Version releases and snapshots
│   ├── v3.0.0/                      # Latest release
│   │   ├── BHI-Workflow-v3.0.0.json          # Black Hebrew Israelite workflow
│   │   ├── BHI-Template-v3.0.0.json          # 20-scene dynamic template
│   │   ├── RELEASE_NOTES_v3.0.0.md           # What's new in this version
│   │   └── CHANGELOG_v3.0.0.md               # Detailed changes
│   ├── v2.1.0/                      # Bible Chapter Generator
│   │   ├── BibleChapterMaster-v2.1.0.json
│   │   ├── BibleChapterTemplate-v2.1.0.json
│   │   └── RELEASE_NOTES_v2.1.0.md
│   └── v1.2.0/                      # Scale Generator
│       ├── ScaleMaster-v1.2.0.json
│       ├── ScaleTemplate-v1.2.0.json
│       └── RELEASE_NOTES_v1.2.0.md
│
├── 🗃️ ARCHIVE/                       # Historical versions and legacy
│   ├── Legacy_Workflows/             # Pre-v1.0 systems
│   └── deprecated/                   # Deprecated components
│
├── 📚 DOCS/                          # Version-controlled documentation
│   ├── v2.1.0/                      # Current doc version
│   └── archive/                     # Previous doc versions
│
└── 🔧 DEVELOPMENT/                   # Development and testing
    ├── experimental/                 # Experimental features
    ├── testing/                     # Test workflows
    └── staging/                     # Pre-production staging
```

---

## 🏷️ **Version Tags and Naming**

### **File Naming Convention**

**Format**: `{ComponentName}-v{MAJOR}.{MINOR}.{PATCH}.{extension}`

**Examples**:
- `BHI-Workflow-v3.0.0.json`
- `BHI-Template-v3.0.0.json`  
- `BibleChapterMaster-v2.1.0.json`
- `ScaleMaster-v1.2.0.json`

### **Component Abbreviations**

- **BHI**: Black Hebrew Israelite
- **BCG**: Bible Chapter Generator
- **SVG**: Scale Video Generator
- **LGW**: Legacy Workflow

---

## 📋 **Version History**

### **v3.0.0 - Black Hebrew Israelite Specialized (Latest)**
**Release Date**: January 2, 2025  
**Breaking Changes**: ✅ Yes - Specialized for Black Hebrew Israelite content

**New Features**:
- ✅ Black Hebrew Israelite specialized AI prompts
- ✅ Melanated skin tone requirements in image generation
- ✅ Traditional Hebrew garment specifications  
- ✅ 20-scene template support
- ✅ Enhanced cultural authenticity features

**Technical Improvements**:
- Enhanced prompt engineering for cultural accuracy
- Improved image generation with specific visual requirements
- Extended scene support (20 scenes)
- Auto-duration timing optimization

### **v2.1.0 - Bible Chapter Generator (Production)**
**Release Date**: June 26, 2025  
**Breaking Changes**: ❌ No - Backward compatible

**New Features**:
- ✅ Production-ready biblical video generation
- ✅ Dynamic timing (46s - 6.5+ minutes)
- ✅ Professional yellow captions
- ✅ Text processing automation
- ✅ Complete documentation suite

### **v1.2.0 - Scale Video Generator (Stable)**
**Release Date**: December 25, 2024  
**Breaking Changes**: ❌ No - Enhancement release

**New Features**:
- ✅ Enhanced overlay text generation
- ✅ CapCut-style subtitles
- ✅ Flux-Pro image generation
- ✅ Make.com-style prompting

---

## 🔄 **Version Control Workflow**

### **Development Process**

1. **Feature Development**: Work in `DEVELOPMENT/experimental/`
2. **Testing**: Move to `DEVELOPMENT/testing/` for validation
3. **Staging**: Pre-production testing in `DEVELOPMENT/staging/`
4. **Release**: Package into `RELEASES/vX.Y.Z/` with release notes
5. **Production**: Deploy to `PRODUCTION/` folder
6. **Archive**: Move old versions to `ARCHIVE/`

### **Documentation Versioning**

**Major Documentation Files** (to be versioned):
- `README.md` → `README-v2.1.0.md`
- `PROJECT_OVERVIEW.md` → `PROJECT_OVERVIEW-v2.1.0.md`
- `SYSTEM_ARCHITECTURE.md` → `SYSTEM_ARCHITECTURE-v2.1.0.md`
- `HANDOVER_COMPLETE.md` → `HANDOVER_COMPLETE-v2.1.0.md`

---

## 🏆 **Best Practices**

### **Version Management**

1. **Always tag releases** with version numbers
2. **Create release notes** for each version
3. **Maintain backward compatibility** when possible
4. **Test thoroughly** before version bumps
5. **Archive old versions** but keep accessible

### **File Organization**

1. **Use consistent naming** across all components
2. **Include version in filename** for clarity
3. **Group related files** in version folders
4. **Maintain clear folder hierarchy**
5. **Document changes** in changelogs

### **Release Process**

1. **Pre-release testing** in staging environment
2. **Version number assignment** following SemVer
3. **Release notes creation** with feature highlights
4. **Production deployment** with monitoring
5. **Post-release validation** and documentation updates

---

## 📞 **Version Support Policy**

### **Support Levels**

- **Current Version (v3.0.0)**: ✅ Full support, active development
- **Previous Major (v2.x.x)**: ✅ Maintenance, critical bug fixes
- **Legacy (v1.x.x)**: ⚠️ Limited support, security fixes only
- **Archived (v0.x.x)**: 📁 No support, reference only

### **Migration Paths**

- **v2.1.0 → v3.0.0**: Cultural specialization upgrade
- **v1.2.0 → v3.0.0**: Full feature upgrade with breaking changes
- **Legacy → v3.0.0**: Complete system replacement

---

## 🚀 **Future Version Management**

### **📋 Complete Step-by-Step Guide**
For detailed instructions on creating new versions, see:
**👉 `FUTURE_VERSION_MANAGEMENT.md`** - Complete guide with templates and examples

### **⚡ Quick Process Overview**
1. **Determine Version Number**: Follow semantic versioning rules
2. **Create Release Folder**: `mkdir RELEASES/vX.Y.Z`
3. **Copy & Rename Files**: Use consistent naming convention
4. **Create Release Notes**: Document all changes and features
5. **Update Documentation**: Add version info to main docs
6. **Test Thoroughly**: Validate before release
7. **Deploy**: Make available in RELEASES folder

### **🎯 Next Version Suggestions**
- **v3.1.0**: Enhanced prompts, additional scene types
- **v3.0.1**: Bug fixes, documentation improvements  
- **v4.0.0**: Major architecture changes, new AI models

---

**📋 RESOURCES**: 
- `FUTURE_VERSION_MANAGEMENT.md` - Detailed version creation guide
- `FOLDER_STRUCTURE_GUIDE.md` - Navigation and organization
- `RELEASES/` folder - All version releases and documentation 
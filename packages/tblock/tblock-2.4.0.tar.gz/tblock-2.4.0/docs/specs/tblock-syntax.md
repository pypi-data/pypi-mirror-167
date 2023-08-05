# TBlock syntax specifications

## Version 2.0 (supported since tblock 2.4.0)

**Introduction**

From version 1.0 Introduction:
> Popular ad blocking formats are not 100% compatible with TBlock. For instance, even though TBlock uses the hosts file to block hosts, there is no way to _allow_ a host in the hosts file format. With AdblockPlus-like formats, there is no way to properly redirect a host to a given IP address. This meant that there was a need for a format fully compatible with TBlock. And here it is.

TBlock syntax version 1.0 was useful, but it was hard to understand it and was prone to a lot of errors. This new specifications aims to make TBlock filter list syntax much clearer and cleaner, as well as improving the size of a filter list written with it.

**Specs**

- There is no need to write a begin and an end statement for rules.
- To specify the policy of a rule, the policy must be written between the `[` and the `]` characters, and the hosts on which the policy is applied must be listed below the policy definition.
- Comments must begin with the `#` character.
- Redirecting IP address must be included inside the policy definition, between two `"` characters.


**Example**

```toml
# This is a comment

[allow]
example.org

[block]
ns1.example.org
ns2.example.org

[redirect "127.0.0.2"]
example.com

[redirect "::1"]
subdomain.example.com
```

## Version 1.0 (deprecated since tblock 2.4.0)

**Introduction**

Popular ad blocking formats are not 100% compatible with TBlock. For instance, even though TBlock uses the hosts file to block hosts, there is no way to _allow_ a host in the hosts file format. With AdblockPlus-like formats, there is no way to properly redirect a host to a given IP address. This meant that there was a need for a format fully compatible with TBlock. And here it is.

**Specs**

- All rules are stored between two tags, `@BEGIN_RULES` and `@END_RULES`. Any line outside this statement will be ignored.
- To specify the policy of a rule, the `!` character must be used, and the hosts on which the policy is applied must be listed below the policy definition.
- Comments must begin with the `#` character.
- Redirecting IP address must follow the policy definition.

**Example**

```yml
>This line will be ignored since it is written before the @BEGIN_RULES statement.

@BEGIN_RULES

# This is a comment

!allow
example.org

!block
ns1.example.org
ns2.example.org

!redirect 127.0.0.2
example.com

!redirect ::1
subdomain.example.com

@END_RULES

>This line will also be ignored since it is written after the @END_RULES statement
```

<p align="center" width="100%">
    <img width="33%" src="https://raw.githubusercontent.com/progrmoiz/Saiki/master/static/img/brand/dark/default.png?token=AIDH6MVN3B2NKTTT6EYC3GLAABUDK" id="saiki"> 
    <br>
</p>

<p align="center">Saiki is modern LMS for universities that focus on improving teachers and students experience.</p>

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

---

## Table of contents
- [Table of contents](#table-of-contents)
- [Modules and Features](#modules-and-features)
- [Installation](#installation)
- [Requirements](#requirements)
- [Build and Run](#build-and-run)
- [Design of the Project](#design-of-the-project)
  * [ERD](#erd)
  * [UML Diagrams](#uml-diagrams)
    + [Activity Diagram](#activity-diagram)
    + [Class Diagram](#class-diagram)
    + [Sequence Diagram](#sequence-diagram)
    + [State Chart Diagram](#state-chart-diagram)
    + [Component Diagram](#component-diagram)
    + [Deployment Diagram](#deployment-diagram)
- [Some Screenshots of Saiki](#some-screenshots-of-saiki)
- [Contributing](#contributing)
- [Contributors ✨](#contributors--)
- [License](#license)

## Modules and Features
- Course
- Notification
- Teachers and Student side
- Stream (forum)
- Announcement
- Assignment
- Result
- Resources

## Installation
 1. Clone the repo https://github.com/progrmoiz/Saiki
 2. Go to the Saiki directory
 3. Create a new database on postgres e.g.: “SAIKI_DB”
 4. Add your db config in `settings.py`
 5. Install [requirements](#requirements) by running `pip install -r requirements.txt`
 6. Create superuser `python manage.py createsuperuser`
 7. [Run the project](#build-and-run) by using  `python manage.py runserver`

## Requirements
To install all required modules use the following command in project dir: `pip install -r requirements.txt`

## Build and Run
To run the project use the following command in project dir: `python manage.py runserver`

## Design of the Project

### ERD
![](https://lh3.googleusercontent.com/40-a4Wqm3S7tJLbnqu0Llg-KiC3rH0TUw4Iog0meoKb4cJnNJSkvd3VhzkwyVu8GNBfL1kq5jgb8Rhvk3m1b8wWSIT6nYkkL0qRBLA_obQrQvRusiQV3o0U2q4DMJDI6fSaoTro)

### UML Diagrams

#### Activity Diagram
![](https://lh6.googleusercontent.com/-RuXdX71cTWo7bENGldw5k10r77eeYZ8rADpNKIR04_sNTwiKNCM6AfuyNgzZxCt9QthjkQ3oSOgDRkB0hjd-M1b9Nz5b7YKNqK2wuavRKsPPTBLQBsbHmv_UZuhfZxNzvspfqo)

#### Class Diagram
![](https://lh4.googleusercontent.com/naPf3mzJvIdus7ZS0xYGdRE_NVz0wymG_gs8MFQoVwBpSnn6p4FM3TWYVvbIW2eOeVHfWO9XHxJLDYltAqFD5obZ8bKkY_-LxUj3uQetfUS1vXS-DhxnX5t4k_z3nvhdR5m2QUI)

#### Sequence Diagram
![](https://lh5.googleusercontent.com/VH4HF3Kjhn4PcxQMazFLXZeY3McWYBqyDqG_Y0fUw6K7iDpOzR6CPDKX3I-XaJQCngwRwQpSsCJJNpS1pa2N71EiNV0ArdXLORd0GoJn4USu6_AP3RHkJntLiv4i-6zKpjq0f24)

#### State Chart Diagram
![](https://lh3.googleusercontent.com/glvnnranFtwc3CdHpG5mBVB_RATObI9hImXOYas62ItHUdeVobcN7ze-7fCZXHdLTYq2DLVnANZvPJ93WLkJLIvNvAp3IxTE5MazRpXAUMVXLNxWYc97sy5orMU08dZpWnFSxWw)

#### Component Diagram
![](https://lh5.googleusercontent.com/aJzZbZwvVgRrcOqdPVaserYo5a4qQTu0nUPl2EluO_09WELgaKZndOg3e-iAa2y56krMksh4swPbsWmn5CWj3VcIiO-93hrJJof-aTYkyD9ZM8vJA0qGWFB0j8jItsApAbLXqEU)

#### Deployment Diagram
![](https://lh3.googleusercontent.com/pj4fE3thw-RnNN7yN4lVi0bVBBDmwFgPCCnMCZRZehm7_OkTHoF3AfASXjcSAroXux5-0bgtx9ZvH-DPzAw-WN10DD_FwxsyhC0EK0joow1sB-HuV46Ed5a2kOGOG9-vr6brxNc)

## Some Screenshots of Saiki

|Login|Announcement|Notification|
|--|--|--|
|  ![Login screen](https://lh3.googleusercontent.com/0Glx8hjtQBpaMGQn2TW2eS_hmtk_wxGeDcUJkDPLe_Y0BqpIC7Gg5e6oVFVM_4kOi_UPlGxFig57bX7D_ygJYRI7viUyf13GYjA06ZCq3VmsTGsypLddhXMWT6Tf20IeeQmxyH8KyigR9d9fNTFPBqtBlUH9Y6QccRup89vy2C4yZLITQiNWiTgpdWy5Of8_xOA0PT-kuWsVuMpMGValPxMk77PXxsU2_DyT8B5JzyEdDgtXKBz4Hw48E9dm9rhEaZpkxEE1f7DFmp3MRrwlv0a1uyfVlnKv2g07hDSzyYnN-J8agXIRuSDwa2NpXSGxiWJQFoYmUrPxIiM8BaQtwwgD7IqIrlf2bOcPtmR4H6wbyFiGCPaZHLc4jdbjMomI0yMuM2tjMvE2LxgL_jskq7j_ZfIZYNgSF_L2cm6ywMyy2hI9CLGdCclgx1edEchjIw5jdJt3wnyTJNSkVq4bNie3rdg6WmtaS_f9mjTQbp9zq7k_hUdC1eX8xYFN54yqn6YQk_qoNn2EqNK9SnbVHSXjtSAg5_7Rs2oNVO9sUPIr1tuDTkX_m1JdFfmDiIUSLRMtLoBq437un5xe-ZIWKcU5WnKozLHz5Mvk9AtclT_uzpDGDRHK2OccAyD1xK-E5tMdbO9arT1X_w8-MHTM_Vl2SkClHxtyVL8qzsYQ0Ix6r1-rAgOX4TQ0QNq3Gg=w1183-h834-no?authuser=0)|  ![Announcement screen](https://lh3.googleusercontent.com/CbOPa00dREehdq4Q8En9ihi0_ZoC2HOiQRcXH1MG5WpSKfWj-zAul_uWernVdJTQKAypoX9bs1Zc1S504tXnqFkj39XYGYo1p0ULMddZsQd9-3uOLVJYQkuqOcpqUlekt0De26-AyF1xZ9uj6BG4bV53-3UdtzPdvpQ_-p_ub1mdnvMoFy6IwEmyWXCRFcDao_w6CUhK4t0g-GhEncl1n0xmHD07FtvJHVj0nMxJ7XAA87STJ5zbCrSjeEd81LGCISoUJojkDcj8nZfSsRFbu7E7PVbyz5wacDXwd1rwBsAOCGiTBsvUoMQE7jqGjWPuccgVBVWyS95nKvBXCVURi4dnmHYSvRdt3FS0yPSfJvye4i2bZTAvol6-7aOo3pSy33w-8Qtf1xDw5eNH8L7P8IbWCzcmgW3YoICxTbmLk4sbqMR3cH42mS2I9Kk0_WnCjzDeBxhQzo8GaQM-qrhjYplSKI8kBeGZezwzxd8U6iLPHhAhN4Vc97OfT5GXqoSGInLuB_xBu7IiReChs_yoFi0FZQaFaBIglT34oI79i87v6ZTTHNVJNMEVnZq9lpQ6gGwF7VTIpL7EOC6Fsc0vtso6jbRG8g19ee0ZgGnfJw8SUCvGv-hDhaJZA0OwFv-Y9d7XokOXVj5p_XFJayi1xiZIAKtw8IkOUxH-dxc64QmoGtiKJ4lx4XroMP9lcg=w1263-h834-no?authuser=0)| ![Notification screen](https://lh3.googleusercontent.com/mgVyTGQ5I2-u1IN19lPz9D7Cy8byOUjOZAcYeZSIcMsZD3naaUkDWtkaWzVNq1BArwpbHx-DYI4u_I74LJSHt-Tnd0CIRl_FM2GzJr2XiF_giXYc9bzT4ZlBcXKgzoNx2F90mvJOwbykFVlrt1eRmEpTpV1N9-Y3NOtNZi--_ZsdMkun49qUQ1iDPB8aXaP0IRFljd74-SWIaQkPmNGQNDfVihuG5mpKzviaGVY4zQx1WRwUI1kZmzu7ES2kmnME9NBrd021ro1VrdTY3uSVBJKfdJb-dvc4AgV5Sq6K3GbEtvEe3GF6HCmEa5jh9_YW0s5epeLvj_YDdFXkMNb4hXNlnCxtE0FhWO-u2P3rn5qgSoUxSyOnX_ny0MR0KWS3DodOfW8iD2gAFCxowT-QBr-tJirHFVpNFJbylZTNsgMaNMCFVdeVRKIg42y690iS2Wy90tQPdc32gIaO56TKpKbVXwrMJfiqG3ZqudOZGFCBwzE-DMl9176_EBaGE2e1hdkSoU8WC7Ax3oBet0H2nTdj1kTCIMxzUvAO5NrFI9xIpIOLqXOrq90ZVPt90FagfSJ4AINeOWK5h-78ZSfqNjXBgkYAhUmWlVhQJBlndX120WQ_OGV04r1xJV8NWmvnGs4Dm9M_sVjrNu-bPUWDtqPvMAPF8qoxnrCGDnjo_l1Pvtb72Eq73CduZewcpQ=w1263-h834-no?authuser=0)|

|View profile |Edit account|Topbar Notification| 
|--|--|--|
|![View profile screen](https://lh3.googleusercontent.com/2ys4rSlWGaSq3laaCFlxN8cdxjdJWVFHvqWfLSqIdTbXlwxzJe8Oi2e1ygiikLLjVLVm3sXdMK21PEASzMmYoJey7BhI9pItzujshz1SF2e_eqLqarlrJRZ9Wvkxm7WkN7PMNlvuJKhsarLO0OucZDpg9u5jdFLTsnb0LEGRW6Drz6jen3nAfa6vXh2u-nbca97XfzUKS-O9IkRSgI5Il4uwwCJDfHnRV6TZWJO0-yu8b646UvUUFeNJP0MrxMBFdpXRRzanvBbv9fttB_EJS80JwW80zcAhLnBdhWYKKTl9WmHyEX79C-8B6t89v4iiMnHis9h2ZYgjVhOVSNG2H8BtFl7AabqIiBiyoSAxqpFsPaa8pxFFdb30RuT7mhmORpFl_DQXtr9QFhM6jPe13LxQ_KOOESiVtm-e9IiUQnD-p5DLALcKwBVRO46IZwEuMNMKPlwl_8Sxs1uTDjHb0EyOW8HPebiifj8IILNeZtq1mfpXsajvuLjl-ubPWlF5M8MrqP0c7ZHaEPkQjERN2RAq_JyFZxWe4CBMRvzGfym9eKNUsLPoQFEkIt_N8pEFc9laxVVltAPQtZkGIW2fdcWTx4Ftnni9d1n6SZ4ohG4Cp0qzb2Vl-B0ic0eOUG-wa7IYkxmNjnodShdujKvBqNEWItRcIRZyEgaiK_VS1PHBT62KFOscpLhdo6MSsg=w1263-h834-no?authuser=0)|![Edit account screen](https://lh3.googleusercontent.com/2ys4rSlWGaSq3laaCFlxN8cdxjdJWVFHvqWfLSqIdTbXlwxzJe8Oi2e1ygiikLLjVLVm3sXdMK21PEASzMmYoJey7BhI9pItzujshz1SF2e_eqLqarlrJRZ9Wvkxm7WkN7PMNlvuJKhsarLO0OucZDpg9u5jdFLTsnb0LEGRW6Drz6jen3nAfa6vXh2u-nbca97XfzUKS-O9IkRSgI5Il4uwwCJDfHnRV6TZWJO0-yu8b646UvUUFeNJP0MrxMBFdpXRRzanvBbv9fttB_EJS80JwW80zcAhLnBdhWYKKTl9WmHyEX79C-8B6t89v4iiMnHis9h2ZYgjVhOVSNG2H8BtFl7AabqIiBiyoSAxqpFsPaa8pxFFdb30RuT7mhmORpFl_DQXtr9QFhM6jPe13LxQ_KOOESiVtm-e9IiUQnD-p5DLALcKwBVRO46IZwEuMNMKPlwl_8Sxs1uTDjHb0EyOW8HPebiifj8IILNeZtq1mfpXsajvuLjl-ubPWlF5M8MrqP0c7ZHaEPkQjERN2RAq_JyFZxWe4CBMRvzGfym9eKNUsLPoQFEkIt_N8pEFc9laxVVltAPQtZkGIW2fdcWTx4Ftnni9d1n6SZ4ohG4Cp0qzb2Vl-B0ic0eOUG-wa7IYkxmNjnodShdujKvBqNEWItRcIRZyEgaiK_VS1PHBT62KFOscpLhdo6MSsg=w1263-h834-no?authuser=0)|![Topbar notification](https://lh3.googleusercontent.com/AAeUddQTl4u12Az6oJyQtuC_Tgz98svune2Ei6flLuvP6HzPYQWtzLHsmvQBRTYLFKNCfh8pbSM8AMcghFovSw6RjA7sYlea5t0MN8vc7Rzc-Bj55JUZ8atZPcx3sfudRNq-yyTYGC4aJnR1JcNbKZQiwOgNe5nz_QoiHaoT4QiGPZ6ES7hvQt3kKiJSU5nGA7TOy_Andpcd0Dq4ha_U156CHT97lPDc1tYP8DHxhKF3VW_g2ymynbQhp9UMXOgrMY0zx5abEVvCd1u1Kw7VBYGNiUBUvODajlilMiUPtcoCm8Wjt-HFTe0Pneo5EbkjmWiHak2EGhZ-xAtPDMaj8iyz8BTk70qgSQSLvbhn462WSKeWcdLVkrS8qLrUyBturaWtF9rbAxErV2FeEiZkL-lRBFG_GLsBfoO30svSHeDANGo85Q0PPXO-zfbuj32Fs8bjvIJeaPGtE9rMxq3bXWhdxEOr888u5iF7ElfZwGSjqlI9cFbpvqcWyHaMXOwGBthIVSY894FY-ymtA_ToOBVN7bwckuxDnfCajspG4G3WPZd07zgGKq6wcL4CMQ131RcYpJxMtti9535q77cUtWMOLEwe6T-3S1yUchmLaX4myzYbucb1i-zUj9ThceRQFA46-gMYPTgp2JBTNXwdUQwwmZ4CxlfA9gl1lEi_nnHL1GH16pAu60Nd8dIEUQ=w1263-h834-no?authuser=0)|

|All courses|Course stream|Course people| 
|--|--|--|
|![All courses screen](https://lh3.googleusercontent.com/9rFQW9Pm2y0TStGTCyqkuaNfH9ye4F0-pdh9J0PTzXHXNONTcwH1taVuZVG_KuArue78_wlDxozBchVypB7hS3RBHWK-4b-k-lUCJoJT5AzMYHS-SNTwH4nP6H1rt0RS7NINQgZfckk-aa5ccEJLPx4j4GrIQX27vhZTNgNY6OFb94C1_qjmHbKt_mIac1vZk_vmRuQ8BC139YHeQ683TypZgeCyYGWJWuBgU_HJqNEN3Eaz2lcHYcOjOGt26S14hti33yUajQpcaXULb80KE6nCsIuXqXAxABmm6Q-lH09iIeyj1BCEAboOb7b3_vz2gonqO5v0S5TG-I8GTeyqoImo139qtAEIOUyedFYBhttceCeT4jIGtoTdElcpeHtaRLoBU1yeMcSN7Wp-DEri0vkMfKqqc_rOuBsil9VO4kENye8WO3m0zbxx1Ve2CdxH0nUtzXj2JkQrcLsMB8iS6tH-4vzEwewbnM8VETmaFT_IJ7KJtzYaHtT1fBPCHggxdEfdPaYIw98YJxYuUO4qrfx8ZORJAEYOQ8pqS33im9zWQXc2eqW22SJFBOTU2PMUH0cqjSkTRmAg5Lhh9-GzSrRcN04yLrDMWJ_HHGrhi-OPcTbU-6TZxhmiroxUx019mAIUX1q3x_6KuPyCZG83OZslUiMyE_s_-JALQjKi7HpR33SJrVC1Lrl0IrZ73w=w1263-h834-no?authuser=0)|![Course stream screen](https://lh3.googleusercontent.com/68hmANchOrhMl7l6_0T4zXnGTBeyBhtvxTrNjsRMhTOS4JEXO2W5d5Isi8vEun8lr8TrTxtnnUGPIyljYhILFwVnjtcDCbHOth9mTho8RtPGFgzJ4uU4KO4N-MPquTAECfHIKxg-tf1Njygw9YKysjd3iPc7oAebjw2_JK6HI9g7IrEZc6HWKSGccLiititwxLpG8LXPvD8T3m_7BKL29rt12UQcdT9pyJ7UrRJAw1BQcSdd3P1Nzfj7lLEs_1gg2aUGYE9nMe6pCJe9Wwjvcmd-EFxc9insXSQXRWXPwzlTRCxmU9uDcmuyIrSexbc9B93CXBksS3AYN1Ga6NYjTgPVecmQEKbZfKbL2ctfKgijX22sE8rtG9X5T6RCiCTzOmm3sxvNUHiLQXH9tfmR6s01Zyizc0LBwjcC1kCrRw3GOOweTO6TuFwHrAv9TTzL9xiYyQVH_1JMXyaywLm7WFnKo5zcRc6KG37F-2YJC3IzFZo1QXmhHKXiUoKm0HSyUyEVYvVzFKiFDllAH2jlxo5L9iMRm8J45O4iTZfajr9QzxESTRCD4jCuEwWXRHJALRvDXzh2WcvA1GZsNjNAGRZFF4zr5a5Wt1dTGAhu6wsXllM1V3TcpIlPF8t2U6cfiBH-kSpO7EjCYIh7glhSFY0Kv3whTDoTcje7dM76AmpKV2QWTtE-P4LCZ3SFDA=w1263-h834-no?authuser=0)|![Course people screen](https://lh3.googleusercontent.com/1_jijGTe0SQc_DZM8UUz4ldWoey3trqPa8KxYAe-8pqoEvYSubOYHRiDFkSdKHvuRVx6pDXat86y-WbTs4Ehc2a4gjvmzzySP3XOn78T7u3FD8yu_o4CvSAmN3Y4oRDBCrnblSeRFwTnu4BVqy3n7ZEeoBdnPzJ3QNWQFnv0PAaLjzU0oYJ0fYTxYoIkLqLo5GRSJdNYkM2i8dW1IbtpWqaadI25H_YrxC39zRzVCcsavhDIjEoKAS1IGCssreMqIeA7D9sH-wnW3P9H6uxZLeAY1HYMwwqG4w7KDNWQ1uiDXmjJOet_tyq_abccPhkSSb1d-ZRJiLXEqI-NRHvDXjgHbO3Jml0OPIpB96Fzc9G9oj3GuFVuqXtiJ-21i3D_cakrB7BHcKWsIV0I6CKN8nPPEgOIBKQ3I-DFgJ-122TECM-HKuZ9L63c-s9rxnCTa56sViFqgLDlB21vto9fMz8Q3AFRN_YiNjwqmnnpLgliVMNoQ2-rJc_uL7zq_dV0gVMrLRYzP-okw3fKi35BkxmoloTx0GfdPadgDpgF5c_OORGXdrDhVHOwvtdCSAASaGYiSfZGIJ3yuZyMs0XmEmoGchLp3N0Fh9BJ7xXBJz6bTFRfn14s96V_eXO9hfPOLvmlM2e9e5IW1C8EdDabH8LKk35JCI70Pzwv7ubVgnDlyAftJDQoXssiIYlFAw=w1263-h834-no?authuser=0)|

|Course assignments|All assignments|Assignment Detail| 
|--|--|--|
|![Course assignments screen](https://lh3.googleusercontent.com/Whe6xqoPpCOod6ZOxj9BxE9fIPMiTp6cQytSWPQYFOUEWfanoUbbmJ3cptThQ7zSEYjvhOcb3ZcWNI8QbjTTP0xoszUCak0G3oPJpIVY-tDcU1tKN5NkVG-1vmRNnNgbP2PrfviSvRxtRvUz-XxwmgrE2pr8UIm4wWZUSAfkmRmUXdwagVGRNK_FVjpMFymcIVTAHR9qf1yoFW87XJ6AKXbh6JU9npEdQr86FLrqbBBDPlCOd1JWxsF_v8M9lTpvVUdnLsjEygaBbYWE7wz3R49t779WRz-Y56mF0I-kMW0X4o2CA7hGJG8Kcms-8iIa8pMHeDT0VhoXBd8AKKosWI6bUPye4Y-iGKxIAvKfFxkAWjqyDzGJfzRgZXmYLiYe5cqR6IwKZ4nOicMDIdMnlatpehI8APp-k4N_k0w2foSEMnpqR0-fyOiAZgXwsHKxiwGuNIdJkIGkH5kJN9rWnE1oQUGjS2pcVnR2v-ltS5MnCrImw9JKfrDYrFCWUBSF2L7js9FRS6tWzWb0UPdfdtfdsxWVdwHNsUPH04-xqyfrhhC3sky9sRrpWaoF01rFQAoXZi809kLvhwL7sry_AMSDPmWcoFRjoLx9D28ZekMJTFpqqtOrqJoRYDZdvxQBCF1CXWI1tIK_A3_GtAZuzCEmFIyy7k3ALdn5dN7VHpI0E_S0FCcbeyTBcGjSjg=w1263-h834-no?authuser=0)|![All assignments screen](https://lh3.googleusercontent.com/QjmEisZ_-TtMdbksUIHUiH1YAHU46Eab06UXiMXOXSQZPM9arDqYLzH46fVG89SAK4NXp-mE69ugcldoiHZdFnYGx0bg7vmMYyzGCm9_tfKB70HMMFlc3HRsMLPpDD-cvEbFhtxUkguIsL1vZ0T30g0CVBuXfIBUxurYRyNEDWnxIXNXdz34mGMeGimNBHjWULTX_dG_MIWHbVHXAx4TtWx09QYKCTojbbuPoEy1kKXrc8YsO2TiyQEgIbJlrzQTgickxh1fskqrGOHMYJG8gZ-3zFm35Q8NW6B8ubBRu7ydvoCZ9ZAIfCAaU9ghtblh4cHlyHa1gflBNsse4n4Re-B0nLWKMSUh5HzcCiyJ1qe0iP-F4q5c_6aPGtHRI0PNnglx2oQSRQ8u2zi8WZ2RHL1ax0G4Y7PkxAdSlKmYYw7IRKzkWeq3AbIh36JUmanZ_T4ABHEd3IxqEHns--IC8VGIuLOy535GxcLCGoP6asy-Wb_5KukTKXF2qT5wAlFlLy3WjMOd8dwA41wqMW77uaJgW1d-_8Y1QSuAqBO4e6q0h4b7voTR3ZR0Dj5KtewQMHhloUFoFvjvqR_gcbaEMYVUUGapezUMPpOMSyiAxl98gVEDRFbkQSYjN8jNCZ8aNjEgzJJdnyoHmiDnrcQMEanAyu5uKNPmTz3JqcjDeKIFln16H__elhf9UBVtWw=w1263-h834-no?authuser=0)|![Assignment detail screen](https://lh3.googleusercontent.com/Ok8UQEFMK0my0w2VZjceITNgt9RuFwr1WiqucT9Jhak7wByZL8JjnO5tnFJbkuC0MetYCV_3a5FNXeiXhyWbI2zT7ZssRAhRfg3i12dewmZUgbvwbQ3FMCIyk0K3pyZnn5n4WG3hS7J9n6hAiZddxThw2ksyJGT9XKmAiXSdJkhxRfDdYB8u4B6S6CkKkXx3kgM0rR6BzJvOo1D20cs4L3vS6fAiRYvbOGZLS7mrQ-XizefEllwEAZB3FhM4XLIHCSYi42Ma5ytVAJQys50i6iF3rs4ne5W_AuDV9sqocjXfcIcqOz5YUp_n5xkr8EJys8HJv6xx599XqOSHPrQvn-AqsQgMAaUBn9NcrTFIi4CBxDccx7ls_thSJ8O3ZeQ6dzsCGHynAK82hXxPrsoMkOIbVmqj0Xz7gGhDu19nmSbdxIRoKEPukLLcOqpfg34dcssX0mpMWFw5cUh8kgcZnJlohGwHnkeHMKVVgcKJoKeNpxT7m4zEURuKTuSDpNxZZm4_3UnZ-hd7cMydQMcPbiWgnye_vGNfEbxmpse4FOcl7ucF1A1QRwE7YvNkGDyaWwyQsQVMV4HQbSkH3hUVyffzOuQqU45Tp8TocW-02-dwUSUavFB1Xsn789TNiO0trdnNnaGRqAH2Wr2dmA1d61ydrUR8kswKcDPZrfTfJ9-6AYAQ0rbkM2vGx_Y4lA=w1263-h834-no?authuser=0)|

|Course resources|Results|Assignments (teacher)| 
|--|--|--|
|![Course resource screen](https://lh3.googleusercontent.com/cIM56ed1Q4SZmVE6p6yu48UhA2bVIwJWhlLoi8SW_Lnqvm0QoKTPXa1Kk9w6ui9qL73K3cQ7JwUcb1pWjeM9hriU6G2DhaS7hB-EvTdEXf1GPs3CB3qP2man-x5DfRq2-WIyUk2tEnzPCSOlHIa7ld0sGBlTkSf1sSFsDbwm99qEJfaa_emJR8ItODr4l37syI1kjaMXod0oDjlkwwHR15dWMdTgGXqrqd7plUivmDhJ-Y8xqBFSz7MW5MJR-J-P4HHI0-kIBVk180_9UAf9CbMpobZ0n-Sg2I9PsHJT4auO2JFYioVeijspi-fhZ_JNaEjP63P_IWd2XfDZh1a5Qb_9NS6UorZ2t4XvZ56vmbkT4FKlwyfnxRYL_5LzzJ-ag1rPPb6E-vr4Tywz7e_UbyAV1dVQJ4RbbmCONEWJKCmYMhPdTBfFM9Ejtn79sRhHmrd3O2knuwCigHuv0Wg-w1NdGW4Wp1P2g2aUWi2EJRsSXkjg7bAw5rK_Ui7Z9K_GZhiRMtHeHp2IeSuKuEV-8cfaTfOGIGf6MORZWx27oEK1EGriIMzeZjTlq_kTMDddwknmgX4tSxExR35ZEyWZA0lTJEVdhwIUwTifmOrhZ5DynScPJYrLBS78h9mZE4-8wl2wyj6Y8xe_P5rF-xduIhPcbEUIxqr3peGSvbO7AyspESZGkgbBMMndV9hl2g=w1263-h834-no?authuser=0)|![Result screen](https://lh3.googleusercontent.com/Aeiy_n19r25jDRnjakris5_y-WOrt3onwU9pObXHxgKRd0IRcxyP0T5zbyZoe5VJXT7YHdNhIewJHxo6LPJWWxc7f1YehXe3T_Zy7tEAPIdF9BfRB8-bgecOgxvxROTO5bL0RA3RTU7StqHOuyJfBB-3JR-Cz-349OMAiDqb5VqTRDBnACULTq6tGj0VPK-yCt6I1fBSC2NZJiNH7V3bRx-6hV2edtVDManyvOBwitz6HDYArZP3UqcfIXl1bdqgoWXv3uBmVhGT-ILxP6T4r9c5xwhPYXx997xG6m-WiqKNwG4mBNY7SL6oeZwPFiphm7o6Cz-eLxGvz8wNDiM-7zXYhNXSoEWiWo18Juc9jLM5uDwMHnrUZfrADdP7HgxLNgefGShAs0iPRNdGnpl_3Td1KQEGBGWhrbm6wG0XHO3CWodJJOdm3kaYXcmIiotRWOGxJpX3Hfo--9_MQttOD5k3NnrR82sz5nYooNoAeTzy8RWF1U9XYeFNnjFiOQihQtK_nFvkJhhqDo5hyJQE1B1qjXrR35VVNxmKjYiF0W4wMheWA5kR4yVjpmqH9wdGAgYTQ4FCmCuHC1B1wPjKCQYauXBKvYp5C8RHoS1bmND_eEal8LGg_Ia4F3Fzs-cbLeSf1WOt74A8A-Zfp-v8msGyfXL75WJkFpqDGmdu65e9SMA5gRj-3_YjdmXbsw=w1263-h834-no?authuser=0)|![Assignment teacher screen](https://lh3.googleusercontent.com/HfYc4I6WDuI23j1cMx-te67Pp6jTdomw4V_Mmn9oOfoiCLsWDMdezD5-m4hgoA1nyY9EsOoYFQNcq2SJWl0uCHUn4YjAeQIsh1EGJEYZ__cfi6FdFx2uMZblWfh05Dz76AyXWlcnHlNGoXtCjM8xxs7Wit2cVhMsHpcr3TP_Q4ynIDJY5pFYtv3GC4dzRZ740RNuoeSDVcHrt5hQ_m-q2EunK_wy5NmC5fe7cKxki6yrRZooQelwSWV0hEvDFyK4CuIpjQ66WaQe6B_AzCn78IGTx0oRGjw9WiSk3SKU3s3J2Sw7V2KEPuykiHBWmtfNQErPKc4QG07xkIpaXkvJb93HlJfH_CfykdvJDwPFoKAdouya4Mj6HY_B8l1DBUbhZ3ULSgfExgg0d_s4vzxmwh-0nV01dn3UMh65BIqkKRQVvju2DxRUn-aISUY23tymqHaBfsRtw68sFqh9yphzFq99yoIuc5UQn_fD-na2wFGWvkDWKVSMy6JsUxjlYO4Zs9Ovw1acZNYh0300WG7Xd_68CR72DpBAnmIO-hS0yrndujCDOw447sCFvVVCOxRWV0tl66vu19lxxDJLFyONN-6hNIrQHX-v3F8pNl66IsEPY8sJw64ie7rb8kOxmAsM0uzEpFAx5SL18lj5t4F--f5H44j8jqEYodFp3qG6-YXztgUkxZObqraeA-Kf3g=w1263-h834-no?authuser=0)|

|Assignment submission (teacher)|Edit assignment (teacher)|Edit grade (teacher)| 
|--|--|--|
|![Assignment submissions screen teacher](https://lh3.googleusercontent.com/RdLq1jJtE8Xy4sbF0Uahs6s8nB1AHqVyqEuxmHpdFXq8YhWmzAsvaLXudgfmTFeYOyswflswUJX8BUyJDmbBudUbsgwe53tFqPwIezpTijpot3yT0PVQh9TSHGdYHXOYPHSRy4ndsAfx2_O-Ng2CLKXUp6gpFa4o8tYEdOTrU3p0uyRJTTjLsAIR2aKX7NLnnmhtFmlysZeCF6dw-weUphOSRYNyIyfdIU7YUbr8xYcHXs5St3E_jLM-BeamyL_2sm8Wszb_-CDQQQySRrGD1RMT7bsGFlC8uTDjBNcG-q31_8qUCfQ6J8nhxtSZZz3szGf5kxw2WiKlRxcd3P04vvl_0ZTjN3ZIZ01Ycrhlj9dWR4wqiK-GakQtCV7zaBrbKJ1UEMdyL9-e-fHeFL_H8NoSsP0oS6E-xP4wzzAPpiHpjNE32CPHmuk4KERxY0XOK_FJ5BaTFsBWRop__83r5Qg246z4qlP2MJUy5lME6A6o0Gk_NQiMD3KLlnSuQlV7-Nf_OyNJJtHDTkoMYyqUKUErDfj3G-GYVMuFfRKsqQIyOJ3Q5pCWCrWOoXlB_aGsOHLPeGRScaUswJTATUMr9LwDQNcYbDQQQug6U8jr6R9FcjWn8ntdljC5NB8B9yxyNg1iyUYnvmDCVhWGd8Eb3TLKAMwRbO6wo6ywcKEnjuD4QE0gdYoW3KHgHyNotg=w1263-h834-no?authuser=0)|![Edit assignment screen teacher](https://lh3.googleusercontent.com/pr9gizhkBmAR_TDuzt1_c9UjIM5RHFEjAZvsCfQnnsXXqiGQX_0JOwRFIn6BF6MO4nzyfYdE0WrcmVMbc8sUJezL4-3u-5jGomYRRZ5KxcSWhezkg7kuLltEzY8p1gPnMcNoNYCfY_aZLy5Us5pQW4snsxOpef_NbsJKJLfhy11SCDOe2j4EdxsvbiXL1FaGdHsqnG3DixARnwhytXdCKFz1hP15Lj1t28GYY-bHfhV0jxuvT4SueCc6-Ul4jBL94S_y8DIjn_qA2P1CVF64x4iIS-_0IHS2ZKFFifkwT9qYs_8nszp8yYeJDANuVWQ0riP4OCrlOryXtYb48NiggdhMnmEtPxCSpTakPg-q3BuKf-JOP3rTEgGORe5-8Un2eRo5avifs7NSj_QMY44FNjkOpQN7pbGmhKYUbISeM59gCfA22PmPtAOcWSYio5HYX9Ad4nS9weROgmxvayDEMoWRe6S0DIY6ppG7H5VigKF-3HarzT6R1XxNn4gyIg8hAEhMkFwm4sh9XNxP9vTGK_uNTjnlwAHfN_irGXLJkd9fCSxWIYrCcKZ9NI5kf-APaPRPUsKcMqyONNqLYlBRogwruAhNrk0L5kpxm-_d192zc4_eMVLBj23v5Libv8qfBV2W3XKOWugeY44scbsBMrmexM7QwkGx_6jG6nozxx8vKsRc2Tzealaq9TKx8A=w1263-h834-no?authuser=0)|![Edit grade screen teacher](https://lh3.googleusercontent.com/znHciu1j1WCMG_KvdjyZ4gecrUcNiJ8veY1-NhVPn925u3hikZL3OmVYw5XNZxfx6RgKVmFa6QNdg3T9ounuPWbMvzgqCz021lA1z8eMVfufyOLL50R8cGez_TkErLHB-2IJkQgJQe9XWqOFQQCYgTclpn-Ks1MYMqi5S1m1VDc1Yp-hS8afDBDgfrQ_XwMlVilM_mjpgQgNxsreZ_RdNGCz28q4-9Y-tULc9gNU_V42WecgkLpRC-CJ-zqXUwjHnwfwFyRPPW1WhMTXC_qU4HnSTlStuiv_oSOhjPHrwsbN8GsF-eugselgAfPG2ZPQllftCcGBNus-VZA7cD6dy-WxrWs8w04zOMG-Qi2dFqVJ_J4zGGmp0-mgT0V14vUIP-FjUIuF8B4fJd_oAwKtCKTmSnXvAmT8MkJ0bzvzYPId2z9_C1-P8D6Gsdfq4fPdsQRYj2YlC6V0txhRgjcxeVLhI0T494BdGZeaHxJcQMo2USTGtYCWDkeJ8qZKfAFeNHcsRLKIggfR3AnS9D0-n2WDl3-jhudCpMVCt0I2xpMhSLGP8srU9aPQkKS1TDgK1krakvyQ6ZDKGTzna0RyNiXQUBRS0rb0D7jPgCF-lpCv8StXq63tTGnu4AHk3RFQPKitE2vpwyG935RXis9XvEsVnI0D1e30obIDoLK0t9YvjSmHtSA5ll3CBV36vw=w1263-h834-no?authuser=0)|

## Contributing
Please check the [CONTRIBUTING.md](CONTRIBUTING.md) file for contribution instructions and naming guidelines.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://abdulmoiz.me"><img src="https://avatars3.githubusercontent.com/u/33980210?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abdul Moiz</b></sub></a><br /><a href="https://github.com/progrmoiz/Saiki/commits?author=progrmoiz" title="Code">💻</a> <a href="#ideas-progrmoiz" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/abdsamadf"><img src="https://avatars2.githubusercontent.com/u/44527855?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abdul Samad</b></sub></a><br /><a href="https://github.com/progrmoiz/Saiki/commits?author=abdsamadf" title="Code">💻</a> <a href="https://github.com/progrmoiz/Saiki/commits?author=abdsamadf" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/muhammad-jawad-92"><img src="https://avatars0.githubusercontent.com/u/63491669?v=4?s=100" width="100px;" alt=""/><br /><sub><b>muhammad-jawad-92</b></sub></a><br /><a href="https://github.com/progrmoiz/Saiki/commits?author=muhammad-jawad-92" title="Code">💻</a> <a href="https://github.com/progrmoiz/Saiki/commits?author=muhammad-jawad-92" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!

## License
Copyright © 2020, [Moiz Farooq](https://github.com/progrmoiz). Released under the [GNU GPLv3](LICENSE).

[:arrow_up: __Back To Top__](#saiki)
